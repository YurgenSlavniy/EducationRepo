import scrapy
from scrapy.http import HtmlResponse
from avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.avito.ru/izhevsk?q={kwargs.get('query')}"]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@data-marker='item-title']")
        for link in links:
            yield response.follow(link, callback=self.parse_ads)


    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', '//h1/span/text()')
        loader.add_xpath('price', "//span[@itemprop='price']/text()")
        loader.add_xpath('photos', "//li[contains(@class,'images-preview-preview')]/img/@src")
        loader.add_value('url', response.url)
        yield loader.load_item()


        # name = response.xpath("//h1/span/text()").get()
        # price = response.xpath("//span[@itemprop='price']/text()").get()
        # url = response.url
        # photos = response.xpath("//li[contains(@class,'images-preview-preview')]/img/@src").getall()
        # yield AvitoparserItem(name=name, price=price, url=url, photos=photos)








