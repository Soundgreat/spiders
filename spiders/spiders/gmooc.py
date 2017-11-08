import scrapy,json
from spiders.items import GCourse

class GMSpider(scrapy.Spider):
    name='gm'
    items=[]
    currentpage=0
    limit=20
    domain='http://mooc.guokr.com/apis/academy/course_list.json'
    params='?order=grading&retrieve_type=by_params&limit=%s&offset=%s'
    base_url=domain+params
    def start_requests(self):
        urls = [
            self.base_url%(self.limit,self.currentpage)
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        data=json.loads(response.body)
        for course in data['result']['courses']:
            item=GCourse()
            item['id']=course['id']
            item['name']=course['name']
            item['school']=course['school']
            item['students']=course['stat']['students_count']
            item['url']=course['url']
            yield item
        #Next page
        if data['result']['courses']:
            self.currentpage=self.currentpage+self.limit
            yield response.follow(self.base_url%(self.limit,self.currentpage),callback=self.parse)