import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from castoramaparcer.items import CastoramaparcerItem
import wget

class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ['https://www.castorama.ru/gardening-and-outdoor/gardening-equipment']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[contains(@class,"next i-next")]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='product-card__img-link']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=CastoramaparcerItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@class='price']/span/span/text()")
        loader.add_xpath('photos', "//li[contains(@class, 'top-slide swiper-slide')]/div/img/@data-src")
        loader.add_value('url', response.url)
        yield loader.load_item()
