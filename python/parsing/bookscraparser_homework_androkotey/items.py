# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksparserItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    authors = scrapy.Field()
    basic_price = scrapy.Field()
    discount_price = scrapy.Field()
    rate = scrapy.Field()