import scrapy


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['https://www.mzitu.com/mm/']
    start_urls = ['http://https://www.mzitu.com/mm//']

    def parse(self, response):
        pass
