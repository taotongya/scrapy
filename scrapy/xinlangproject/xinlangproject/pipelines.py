# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XinlangprojectPipeline(object):
    def process_item(self, item, spider):
        # 提取sonUrls出来并修改成需要的文件名格式
        sonUrls = item['sonUrls']
        filename = sonUrls[7:-6].replace('/', '_')
        filename += '.txt'

        fullFilename = item['subFilename'] + '/' + filename
        print('文件写入:', fullFilename)
        f = open(fullFilename, 'w', encoding='utf-8')
        content = item['content']
        f.write(str(content.encode('utf-8'), encoding='utf-8'))
        f.close()


        return item
