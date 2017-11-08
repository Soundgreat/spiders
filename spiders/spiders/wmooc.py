import scrapy
from spiders.items import WCourse

class WMSpider(scrapy.Spider):
    name='wm'
    currentpage=1
    items=[]
    base_url='http://study.163.com/courses#/?pt=0&p=%d'
    def start_requests(self):
        urls=[]
        for i in range(1,61):
            urls.append(self.base_url%i)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        items=[]
        courses=response.css('a[href*=series]')
        for course in courses:
            item=WCourse()
            item['name']=course.xpath('@data-name').extract_first()
            item['category']=course.xpath('@data-index').extract_first()
            item['url']=course.xpath('@href').extract_first()
            yield item
        #Next page
        # if self.currentpage<60:
        #     self.currentpage=self.currentpage+1
        #     yield response.follow(self.base_url%self.currentpage,callback=self.parse)