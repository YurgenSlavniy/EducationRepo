# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class BooksparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client['books_hw6']

    def process_item(self, item, spider):

        item['_id'] = self.process_id(item['url'])
        item['title'] = self.process_title(item['title'])
        item['authors'] = self.process_authors(item['authors'])
        item['basic_price'] = self.process_basic_price(item['basic_price'])
        item['discount_price'] = self.process_discount_price(item['discount_price'])
        item['rate'] = self.process_rate(item['rate'])

        try:
            collection = self.mongobase[spider.name]
            collection.insert_one(item)
        except DuplicateKeyError:
            print('#' * 20 + '\nД\nУ\nБ\nЛ\nИ\nК\nА\nТ\n' + '#' * 20)

        return item

    def process_id(self, url):
        return hashlib.sha224(url.encode()).hexdigest()[0:20]

    def process_authors(self, authors):
        return ', '.join([a.strip() for a in authors if a != ', '])

    def process_title(self, title):
        return title.strip()

    def process_basic_price(self, basic_price):
        return int(basic_price.strip().replace('\xa0', '').replace(' ₽', '')) if basic_price else None

    def process_discount_price(self, discount_price):
        return int(discount_price.strip().replace('\xa0', '').replace(' ₽', '')) if discount_price else None

    def process_rate(self, rate):
        return float(rate.strip().replace(',', '.')) if rate else None