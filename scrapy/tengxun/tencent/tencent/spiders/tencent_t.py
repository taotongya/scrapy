# -*- coding: utf-8 -*-
import scrapy
from tencent.items import *

class TencentTSpider(scrapy.Spider):
    name = 'tencent_t'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]
    def parse(self, response):
        items =[]
        #职位
        php = response.xpath('//table[@class="tablelist"]//tr/td/a/text()').extract()
        #职位类型
        type = response.xpath('//table[@class="tablelist"]//tr[@class="even"]/td[2]/text()').extract()
        #人数
        number = response.xpath('//table[@class="tablelist"]//tr[@class="even"]/td[3]/text()').extract()
        #地点
        location = response.xpath('//table[@class="tablelist"]//tr[@class="even"]/td[4]/text()').extract()
        #发布时间
        time = response.xpath('//table[@class="tablelist"]//tr[@class="even"]/td[5]/text()').extract()
        # print('职位:',php,'职业类型:',type,'人数:',number,'地点:',location,'发布时间:',time)

        for i in range(len(time)):
            item = TencentItem()
            item['php'] = php[i]
            item['type'] = type[i]
            item['number'] = number[i]
            item['location'] = location[i]
            item['time'] = time[i]
            items.append(item)
            yield item

        if self.offset <=2691 :
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)