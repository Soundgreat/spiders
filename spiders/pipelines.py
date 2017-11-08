# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,time

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('{}{}.json'.format(spider.name,time.strftime("%H-%M-%S", time.localtime())),'w',encoding='utf-8')

    def close_spider(self, spider):
        json.dump(spider.items,fp=self.file,ensure_ascii=False,sort_keys=True,indent=4,separators=(',',':'))
        self.file.close()

    def process_item(self, item, spider):
    	spider.items.append(dict(item))
    	return item