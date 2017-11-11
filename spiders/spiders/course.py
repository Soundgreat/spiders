import scrapy,json
from spiders.items import Course

class CourseSpider(scrapy.Spider):
    name='course'
    limit=20
    currentpage=0
    domain='http://mooc.guokr.com'
    params='/apis/academy/course_list.json?order=grading&retrieve_type=by_params&limit=%s&offset=%s'
    base_url=domain+params
    def start_requests(self):
        urls = [
            self.base_url%(self.limit,self.currentpage)
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse_list)

    def parse_list(self, response):
        data=json.loads(response.body, encoding='utf-8')
        for course in data['result']['courses']:
            item = Course()
            try:
                item['id'] = course['id']
            except:
                item['id'] = None
            try:
                item['name']=course['name']
            except:
                item['name'] = None
            try:
                item['schoolId']=course['school_id']
            except:
                item['schoolId'] = None
            try:
                item['school']=course['school']
            except:
                item['school'] = None
            try:
                item['students']=course['stat']['students_count']
            except:
                item['students'] = None
            try:
                item['followers']=course['stat']['followers_count']
            except:
                item['followers'] = None
            try:
                item['replies']=course['stat']['replies_count']
            except:
                item['replies'] = None
            try:
                item['posts']=course['stat']['posts_count']
            except:
                item['posts'] = None
            try:
                item['articles']=course['stat']['articles_count']
            except:
                item['articles'] = None
            try:
                item['certification']=course['certification']
            except:
                item['certification'] = None
            try:
                item['url']=course['url']
            except:
                item['url'] = None
            yield scrapy.Request(url=item['url'], callback=self.parse_details, meta={'item': item})
        #Next page
        if data['result']['courses']:
            self.currentpage=self.currentpage+self.limit
            yield scrapy.Request(url=self.base_url%(self.limit,self.currentpage),callback=self.parse_list)

    def parse_details(self, response):
        item=response.meta['item']
        try:
            scoreAverageInt = int(response.css('span.course-score-average::text').extract_first()[:-1])
            scoreAverageFloat = int(response.css('span.course-score-average small::text').extract_first())
            scoreAverage = scoreAverageInt + scoreAverageFloat / 10
            item['scoreAverage']=scoreAverage
        except:
            item['scoreAverage'] = None
        try:
            scorePeople = int(response.css('span.course-score-people::text').extract_first()[1:-2])
            item['scorePeople'] = scorePeople
        except:
            item['scorePeople'] = None
        try:
            talentUrl = response.css('div.talent_box a.talent::attr(href)').extract_first()
            item['talentUrl'] = self.domain + talentUrl
        except:
            item['talentUrl'] = None
        yield item