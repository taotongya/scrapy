# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
from urllib import  request
class BaomaPipeline(object):
    def __init__(self):
        #   os.path.dirname(__file__)   获取当前工程的目录
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')  #os.path.join 拼接目录，创建名为images 的目录
        if not os.path.exists(self.path):   #  os.path.exists 判断 某路径是否存在
            os.mkdir(self.path)
        else:
            pass
    def process_item(self, item, spider):
        catpi = item['catpi']
        urls = item['urls']
        catpi_path = os.path.join(self.path,catpi)
        if not os.path.exists(catpi_path):
            os.mkdir(catpi_path)
        for url in urls:
            #以下划线切割 获取图片的名字
            imagea_name = url.split('_')[-1]
            #下载图片到相应目录
            # images 目录下的图片分类目录
            request.urlretrieve(url,os.path.join(catpi_path,imagea_name))

        return item


class BaomaImagesPipeline(ImagesPipeline):
    pass