import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from ..search_query import search_text


class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = [f'https://www.superjob.ru/vacancy/search/?keywords={search_text}&noGeo=1']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[contains(@class, 'Dalshe')]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath(f"//div[@class='f-test-search-result-item']{'/div'*7}/span/a/@href").getall()
        for link in links:

            yield response.follow('https://spb.superjob.ru' + link, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):
        name = response.css("h1::text").get()
        city = response.xpath("//div[contains(@class, 'address')]/span/span//text()").getall()
        salary = response.xpath("//div[contains(@class, 'address')]/../span//text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url, city=city)