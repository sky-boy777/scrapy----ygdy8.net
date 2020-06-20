# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class Dytt8Spider(CrawlSpider):
    name = 'dytt8'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/']

    rules = (
        # 电影详情页链接
        Rule(LinkExtractor(restrict_xpaths='//a[@class="ulink"]'), callback='movie_detail'),
        # 下一页的链接
        Rule(LinkExtractor(allow=r'list_23_([0-9]+).html'), follow=True),
    )

    def movie_detail(self, response):
        '''在电影详情页提取电影信息'''
        item = {}
        item["name"] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first()

        # 下面是使用正则匹配（这个网站的网页太不规范了）
        response_str = response.text
        # 产地
        place = re.findall(r'<br />◎产　　地　(.*?)<br />', response_str)
        item["产地"] = place[0] if len(place) > 0 else None
        # 年代
        time = re.findall(r'<br />◎年　　代　(.*?)<br />', response_str)
        item["年代"] = time[0] if len(time) > 0 else None
        # 简介
        brief = re.findall(r'<br />◎简　　介 <br /><br />　　(.*?)<br />', response_str)
        item["简介"] = brief[0] if len(brief) > 0 else None

        # url
        item["url"] = response.url
        yield item






