# spiders
## How to start
    1.$ scrapy crawl courses
    2.$ scrapy crawl students [-a coursefile=filename]

You should execute the commands above in the project **root** folder in order.
Notice that the *coursefile* argument is optional, from which we can get some data for the next spider and continue to crawl more.
It comes with a default value('courses.json')
which is an existed json file(inside *data* folder) contains the course data I crawled before 
and you can specify another file crawled by yourself.