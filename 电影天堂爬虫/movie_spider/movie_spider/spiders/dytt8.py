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
        """在电影详情页提取电影信息"""
        item = dict()
        try:
            # 电影简介
            item['title'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first()

            # 电影名
            name = re.search(r'《(.*?)》', item.get('title'))
            if name:
                item['name'] = name.group(1)
            else:
                item['name'] = 'null'

            # 电影天堂发布此电影时间
            time = response.xpath('//div[@class="co_content8"]/ul/text()').get()
            if re.search(r'发布时间：(\d+-\d+-\d+)', time):
                time = re.search(r'发布时间：(\d+-\d+-\d+)', time).group(1)
            else:
                time = '1000-01-01'
            item['time'] = time

            # 电影封面图url
            image = response.xpath('//div[@id ="Zoom"]//img[@border="0"]/@src').get()
            item['image'] = image if image else ''

            # 电影详情页
            detail = response.xpath('//div[@id="Zoom"]//td').get()
            item['detail'] = detail if detail else 'null'

            # 原网站url
            item["url"] = response.url

            # 下面是使用正则匹配
            response_str = response.text

            # 豆瓣评分
            douban_score = re.findall(r'◎豆瓣评分　(.*?)/10', response_str)
            try:
                douban_score = float(douban_score[0])
            except:
                douban_score = -1
            item['douban_score'] = douban_score

            # IMDb评分
            IMDb_score = re.findall(r'◎IMDb评分　(\d.\d)?/10', response_str)
            try:
                IMDb_score = float(IMDb_score[0])
            except:
                IMDb_score = -1
            item['IMDb_score'] = IMDb_score

            yield item
        except:
            yield item






