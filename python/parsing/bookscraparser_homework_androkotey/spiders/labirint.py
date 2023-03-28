import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem
from booksparser.search_query import search_text


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = [f'https://www.labirint.ru/search/{search_text}/?stype=0']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//div[@class='pagination-next']//@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='cover']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response: HtmlResponse):
        title = response.css("h1::text").get()
        authors = response.xpath("//div[@class='authors']//a//text()").getall()
        basic_price = response.xpath("//span[@class='buying-priceold-val-number']//text()").get()
        discount_price = response.xpath("//span[@class='buying-pricenew-val-number']//text()").get()
        rate = response.css("#rate::text").get()
        url = response.url
        yield BooksparserItem(title=title, basic_price=basic_price,
                              discount_price=discount_price, url=url,
                              authors=authors, rate=rate)