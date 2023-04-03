import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem
from booksparser.search_query import search_text


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    i = 1
    start_urls = [f'https://book24.ru/search/page-{i}/?q={search_text}']

    def parse(self, response: HtmlResponse):
        Book24Spider.i += 1
        next_page = f'https://book24.ru/search/page-{Book24Spider.i}/?q={search_text}'
        if response.status != 404:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//div[@class='product-list__item']//a[@class='product-card__name smartLink']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response: HtmlResponse):
        title = response.css("h1::text").get()
        if 'Успенский Эдуард Николаевич' in title:
            print()
        authors = response.xpath("(//span[contains(text(), 'Автор')]/../following-sibling::*[1])[1]//text()").getall()
        basic_price = response.xpath("//span[@class='app-price product-sidebar-price__price']/text()").get()
        discount_price = response.xpath("//span[contains(@class, 'price-old')]/text()").get()
        rate = response.xpath("//span[@class='rating-widget__main-text']/text()").get()
        url = response.url
        yield BooksparserItem(title=title, basic_price=basic_price,
                              discount_price=discount_price, url=url,
                              authors=authors, rate=rate)