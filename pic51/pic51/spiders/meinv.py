from copy import deepcopy
from urllib.parse import urljoin
import scrapy
from ..items import Pic51Item
import logging
import urljoin

logger = logging.getLogger(__name__)


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['http://59pic.92demo.com/mn/']
    start_urls = ['http://59pic.92demo.com/mn/']

    def parse(self, response):
        # nodes = response.xpath('/html/body/div[7]')
        # logger.warning(nodes.extract())
        # for node in nodes:
        #     detail_url_list = node.xpath('//*[@id="load-img"]/ul/li/a/@href').extract()
        #     # logger.warning(detail_url_list)
        #     for detail_url_html in detail_url_list:
        #         detail_url = urljoin('http://59pic.92demo.com/', detail_url_html)
        #         # logger.warning(detail_url)
        #         if not detail_url:
        #             return
        yield scrapy.Request('http://59pic.92demo.com/mn/1105.html', callback=self.parse_detail, dont_filter=True)
        #       yield scrapy.Request(detail_url, callback=self.parse_detail, dont_filter=True)
        # nodes = response.xpath('//*[@id="load-img"]')
        # next_url = 'http://59pic.92demo.com' + nodes.xpath('//*[@id="pageNum"]/span/a/@href').extract_first()
        # if not next_url:
        #     return
        # yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
        # 传入下一页链接并且再次解析
        # logger.warning(next_url)
        # yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)

    # 详情页解析函数
    def parse_detail(self, response):
        # logger.warning(response.url)
        item = Pic51Item()
        nodes = response.xpath('/html/body/div[3]/div[1]')
        for node in nodes:
            # 解析要保存的图片地址
            html_name = node.xpath('/html/body/div[3]/div[1]/div[1]/text()[3]').extract_first()
            item['explore_name'] = html_name[3:-1]
            image_alt = node.xpath('//*[@id="bigImg"]/@alt').extract_first()
            item['image_alt'] = image_alt
            image_url = node.xpath('//*[@id="bigImg"]/@src').extract_first()
            item['image_url'] = image_url
            logger.warning(item)
            yield item
        # next_image_html = nodes.xpath('//*[@id="pageNum"]/span/a[8]/@href').extract_first()
        next_image_html = nodes.xpath('//*[@class="pageNext"]/@href').extract_first()
        if not next_image_html:
            return
        next_url = 'http://59pic.92demo.com/' + next_image_html
        # logger.warning(next_image_url)
        yield scrapy.Request(next_url, callback=self.parse_detail_next,meta={'item':deepcopy(item)},dont_filter=True)

    def parse_detail_next(self, response):
        item = response.meta.get('item')
        nodes = response.xpath('/html/body/div[3]/div[1]')
        for node in nodes:
            # 解析要保存的图片地址
            html_name = node.xpath('/html/body/div[3]/div[1]/div[1]/text()[3]').extract_first()
            # logger.warning(len(html_name))
            item['explore_name'] = html_name[3:-1]
            image_alt = node.xpath('//*[@id="bigImg"]/@alt').extract_first()
            # logger.warning(len(image_alt))
            item['image_alt'] = image_alt
            image_url = node.xpath('//*[@id="bigImg"]/@src').extract_first()
            item['image_url'] = image_url
            logger.warning(item)
            yield item
        next_image_html = nodes.xpath('//*[@class="pageNext"]/@href').extract_first()
        # logger.warning(next_image_html)
        if not next_image_html:
            return
        next_image_url = 'http://59pic.92demo.com/' + next_image_html
        yield scrapy.Request(next_image_url, callback=self.parse_detail_next, meta={'item': deepcopy(item)},
                             dont_filter=True)
