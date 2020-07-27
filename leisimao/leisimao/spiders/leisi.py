import scrapy
import re
import logging
from ..items import LeisimaoItem


logger = logging.getLogger(__name__)

class LeisiSpider(scrapy.Spider):
    name = 'leisi'
    allowed_domains = ['https://www.lesmao.org/']
    start_urls = ['https://www.lesmao.org/']

    def parse(self, response):
        # print(response.text)
        ret = response.xpath('//*[@id="index-pic"]/div/div[1]/a//@href').extract()
        # print(ret)
        # logger.warning(ret)
        for html in ret:
            # logger.warning(html)
            for i in range(1,6):   
                item = LeisimaoItem()  
                sro = html.replace('-1-', '-{}-').format(i)
                item['url'] = 'https://www.lesmao.org/' + sro
                # logger.warning(url_list)
                yield item


