# -*- coding: utf-8 -*-
import scrapy
from baoma.items import *

class Baoma5Spider(scrapy.Spider):
    name = 'baoma5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://www.4444af.com/html/artlist/katongdongman/27.html']

    def parse(self, response):
        boxurls = response.xpath('//div[@class="uibox"]')[1:]
        for boxurl in boxurls:
            catpi = boxurl.xpath('.//div[@class="uibox-title"]/a/text()').get()
            urls = boxurl.xpath('.//ul/li/a/img/@src').getall()

            urls = list(map(lambda url:response.urljoin(url),urls))
            # for url in urls:
            #     url = response.urljoin(url)   #自动拼接成完整的url
            #     # url = 'https:'+url
            #     print(url)
            item = BaomaItem(catpi=catpi,image_urls=urls)
            yield item