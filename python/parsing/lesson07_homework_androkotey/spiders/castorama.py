import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from castoparser.items import CastoparserItem
from castoparser.search_query import search_text


class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']
    start_urls = [f'https://www.castorama.ru/catalogsearch/result/?q={search_text}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("(//a[@class='next i-next']/@href)[1]").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[contains(@class, 'product-card')][2]/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoparserItem(), response=response)
        loader.add_css('name', 'h1::text')
        loader.add_xpath('price', "(//span[@class='currency']/../span[1])[1]/text()")
        loader.add_xpath('photos', "//img[contains(@class, 'top-slide__img')]/@data-src")
        loader.add_value('url', response.url)
        yield loader.load_item()
