import scrapy
from ..items import Pic51Item
import logging
from copy import deepcopy
import urljoin
logger = logging.getLogger(__name__)
class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['http://59pic.92demo.com/']
    start_urls = ['http://59pic.92demo.com/']

    def parse(self, response):
        nodes = response.xpath('//*[@id="load-img"]')
        # logger.warning(next_url)
        for node in nodes:
            item = Pic51Item()
            detail_url =  urljoin(response.url, nodes.xpath('//*[@id="load-img"]/ul/li/a/@href').extract_first())
            # print(item)
            item['detail_url'] = detail_url_list
            # for detail_html in detail_url_list:
                # 获取详情页链接
            # Sdetail_html_url = 'http://59pic.92demo.com' + detail_html
                # logger.warning(detail_html_url)
                # 将详情页链接传入详情解析函数并且回调
                # yield scrapy.Request(detail_html_url, callback=self.parse_detail, meta={'item':deepcopy(item)})
        # 下一页链接构造
        next_url ='http://59pic.92demo.com' + str(nodes.xpath('//*[@id="pageNum"]/span/a/@href').extract_first())
        # if not next_url:
        #     return    
        # 传入下一页链接并且再次解析
        # logger.warning(next_url)
        yield scrapy.Request(next_url, callback=self.parse)

    # 详情页解析函数
    def parse_detail(self, response):
        item = item.meta.get('item')
        logger.warning(response.url)
