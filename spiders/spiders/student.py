import scrapy, json, os
from spiders.items import Student

class StudentSpider(scrapy.Spider):
    name = 'students'
    domain = 'https://mooc.guokr.com'
    coursesList = []
    urls = []
    def __init__(self, coursefile='courses.json', *args, **kwargs):
        super(StudentSpider, self).__init__(*args, **kwargs)
        filepath = os.path.abspath(__file__ + "/../../../data/" + coursefile)
        with open(filepath, 'rb') as file:
            self.coursesList = json.load(file)
        for i in range(0,len(self.coursesList)):
            if self.coursesList[i]['talentUrl'] != None:
                self.urls.append(self.coursesList[i]['talentUrl'])

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse_homepage)

    def parse_homepage(self, response):
        item=Student()
        try:
            item['id'] = int(response.css('div.certificate_box a.certificate-script::attr(href)').extract_first()[-1-10:-1])
        except:
            item['id'] = None
        try:
            item['education'] = response.css('div.education p::text').extract_first()[1:3]
        except:
            item['education'] = None
        try:
            item['certificates'] = int(response.css('div.certificate_box span.title-attached::text').extract_first()[1:-2])
        except:
            item['certificates'] = None
        try:
            item['coursesFoused'] = int(response.css('div.course_box h3.course-list-title a span::text').extract()[0])
        except:
            item['coursesFoused'] = None
        try:
            item['coursesLearned'] = int(response.css('div.course_box h3.course-list-title a span::text').extract()[1])
        except:
            item['coursesLearned'] = None
        try:
            item['comments'] = int(response.css('div.me-info ul.me-nav li span::text').extract()[0])
        except:
            item['comments'] = None
        try:
            item['notes'] = int(response.css('div.me-info ul.me-nav li span::text').extract()[1])
        except:
            item['notes'] = None
        try:
            item['discussions'] = int(response.css('div.me-info ul.me-nav li span::text').extract()[2])
        except:
            item['discussions'] = None
        try:
            item['collections'] = int(response.css('div.me-info ul.me-nav li span::text').extract()[3])
        except:
            item['collections'] = None
        try:
            coursesFousedListUrl = self.domain+response.css('div.course_box h3.course-list-title a::attr(href)').extract()[0]
        except:
            coursesFousedListUrl = None
        try:
            coursesLearnedListUrl = self.domain+response.css('div.course_box h3.course-list-title a::attr(href)').extract()[1]
        except:
            coursesLearnedListUrl = None
        try:
            commentsListUrl = self.domain+response.css('div.cmt_more a::attr(href)').extract_first()
        except:
            commentsListUrl = None
        yield scrapy.Request(url=commentsListUrl,callback=self.parse_commentsList, meta={'item': item})

    def parse_commentsList(self, response):
        item = response.meta['item']
        item['commentsList']=[]
        commentsList = response.css('div.comment_box ul.comment_list li')
        for i in range(0,len(commentsList)):
            cmtCourseUrl = response.css('div.comment_box ul.comment_list li')[i].css('div.cmt-course a::attr(href)').extract_first()
            cmtSum = response.css('div.comment_box ul.comment_list li')[i].css('p.cmt-content::text').extract_first()
            item['commentsList'].append({'cmtCourseUrl': cmtCourseUrl,'cmtSum': cmtSum})
        yield item