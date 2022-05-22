# -*- coding: utf-8 -*-

# Scrapy settings for movie_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie_spider'

SPIDER_MODULES = ['movie_spider.spiders']
NEWSPIDER_MODULE = 'movie_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 设置请求头
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

# 日志提示等级
LOG_LEVEL = "WARNING"

# 项目管道
ITEM_PIPELINES = {
    'movie_spider.pipelines.MovieSpiderPipeline': 300,
}


# redis分布式爬虫主要做下面几点，需要安装pip install scrapy-redis
# 一个去重的类，用来将url去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否持久化
SCHEDULER_PERSIST = True
# redis地址
REDIS_URL = "redis://127.0.0.1:6379/0"


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 节流阀，自动调整下载延迟
#AUTOTHROTTLE_ENABLED = True

# 初始下载延迟，默认5
AUTOTHROTTLE_START_DELAY = 5

# 在高延迟情况下设置的最大下载延迟，默认60
AUTOTHROTTLE_MAX_DELAY = 60

# 机器人协议，false表示不遵守，在网站下/robots.txt可以看到
ROBOTSTXT_OBEY = False

# Scrapy应该并行发送到每个远程服务器的请求的平均数量
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
