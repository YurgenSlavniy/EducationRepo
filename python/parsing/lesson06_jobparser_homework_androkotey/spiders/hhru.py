import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from jobparser.search_query import search_text


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [f'https://spb.hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&text={search_text}&from=suggest_post&clusters=true&ored_clusters=true&enable_snippets=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//a[@data-qa="vacancy-serp__vacancy-title"]/@href').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_vacancy)

    def parse_vacancy(self, response: HtmlResponse):
        name = response.css("h1::text").get()
        city = response.xpath("//*[contains(@data-qa, 'location')]//text()").getall()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        url = response.url
        yield JobparserItem(name=name, salary=salary, url=url, city=city)