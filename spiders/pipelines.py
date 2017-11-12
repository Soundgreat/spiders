# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, time, os

class JsonWriterPipeline(object):
    items = []
    def open_spider(self, spider):
        filename='{}{}.json'.format(spider.name,time.strftime("%H-%M-%S", time.localtime()))
        datafolder = os.path.abspath(__file__ + '/../../data')
        if not os.path.exists(datafolder):
            os.makedirs(datafolder)
        filepath= os.path.join(datafolder, filename)
        self.file = open(filepath,'w',encoding='utf-8')

    def close_spider(self, spider):
        json.dump(self.items,fp=self.file,ensure_ascii=False,sort_keys=False,indent=4,separators=(',',':'))
        self.items = []
        self.file.close()

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item