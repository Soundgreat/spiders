# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Course(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    schoolId=scrapy.Field()
    school=scrapy.Field()
    students=scrapy.Field()
    followers=scrapy.Field()
    replies=scrapy.Field()
    posts=scrapy.Field()
    articles=scrapy.Field()
    certification=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    scoreAverage=scrapy.Field()
    scorePeople=scrapy.Field()
    talentUrl=scrapy.Field()

class Student(scrapy.Item):
    id=scrapy.Field()
    certificates=scrapy.Field()
    coursesFoused=scrapy.Field()
    coursesFousedList=scrapy.Field()
    coursesLearned=scrapy.Field()
    coursesLearnedList=scrapy.Field()
    commentsList=scrapy.Field()
    comments=scrapy.Field()
    notes=scrapy.Field()
    discussions=scrapy.Field()
    collections=scrapy.Field()
    education=scrapy.Field()