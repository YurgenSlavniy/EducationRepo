from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.superjob import SuperjobSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    runner.crawl(HhruSpider)
    runner.crawl(SuperjobSpider)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()
