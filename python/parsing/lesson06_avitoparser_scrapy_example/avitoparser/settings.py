# Scrapy settings for avitoparser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'avitoparser'

IMAGES_STORE = 'photos'
IMAGES_THUMBS = {
   'medium': (55, 35)
}


SPIDER_MODULES = ['avitoparser.spiders']
NEWSPIDER_MODULE = 'avitoparser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'cookie':'yandexuid=1259160151646070856; yuidss=1259160151646070856; yabs-sid=1937487681646070856; ymex=1961430856.yrts.1646070856#1961430856.yrtsi.1646070856; gdpr=0; _ym_uid=1646070893156269093; my=YwA=; amcuid=8340317491646422388; yandex_login=Orleon.ya; i=wdTJiryHb+LLnT5mcRSlLhkbNWoRkyWlPsQzRYQZNAx4MhNo6TM/BV8R51m0d0jIkpBJv0xmNtTmxeXkiTiWht9wDgw=; is_gdpr=0; is_gdpr_b=CNaZZBDuaigC; yandex_gid=44; cycada=Pu5H3ElFTWHQAAU7lrMwAL/hvOtk0vJNciYyzRBtN1E=; _ym_d=1649519883; yabs-frequency=/5/0000000000000000/LVTwO9j8Vb84HY6q2tDmb00000H68M-bN1mQii9h14Od8krF10oancu4HYC0/; yp=1665287886.szm.1_25:2560x1440:1990x1072#1962472582.udn.cDpPcmxlb24ueWE%3D#1651771282.ygu.1#1651771283.spcs.l#1651857692.csc.1; ys=udn.cDpPcmxlb24ueWE%3D#c_chck.8048816; Session_id=3:1649696374.5.0.1647112582511:GiqSWw:25.1.2:1|271833109.0.2|3:250771.178521.H07E8OxfqD1kCKQ9zmuC7qex_qY; sessionid2=3:1649696374.5.0.1647112582511:GiqSWw:25.1.2:1|271833109.0.2|3:250771.178521.H07E8OxfqD1kCKQ9zmuC7qex_qY'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'avitoparser.middlewares.AvitoparserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'avitoparser.middlewares.AvitoparserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'avitoparser.pipelines.AvitoparserPipeline': 300,
   'avitoparser.pipelines.AvitoPhotosPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
