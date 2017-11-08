# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GCourse(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    url=scrapy.Field()
    name=scrapy.Field()
    school=scrapy.Field()
    students=scrapy.Field()
    #last_updated = scrapy.Field(serializer=str)

class WCourse(scrapy.Item):
	name=scrapy.Field()
	category=scrapy.Field()
	url=scrapy.Field()