import requests
from lxml import etree
import time
import random
import re

#  确定url
url = 'http://www.shuquge.com/txt/91629/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36',
    'Referer': 'http://www.shuquge.com/txt/91629/21121025.html'
}
response = requests.get(url, headers=headers).content.decode('utf-8')


# print(response)
# 定义一个函数用来获取所有网页链接
def get_html():
    html_data = etree.HTML(response)
    ret = html_data.xpath('/html/body//a/@href')[39:712]
    # print(ret)
    return ret


# 定义一个函数用来请求所有的链接并获取每一章的内容
def get_data():
    html_list = get_html()
    # print(html_list)
    # url_list = []
    for html in html_list:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36',
            'Referer': 'http://www.shuquge.com/txt/91629/21121025.html'
        }
        urls = 'http://www.shuquge.com/txt/91629/' + str(html)
        # url_list.append(urls)
        text_data = requests.get(urls, headers=header).content.decode('utf-8')
        # time.sleep(random.random())
        # print(text_data) 获取章节内容
        text_date = (etree.HTML(text_data))
        title = str(text_date.xpath('//*[@id="wrapper"]/div[4]/div[2]/h1/text()')[0])
        # print(title)
        with open('会穿越的道观.txt', 'a') as f:
            f.write(title)
        texts = str(text_date.xpath('//*[@id="content"]/text()'))
        text_list = re.findall(r"\\xa0\\xa0\\xa0\\xa0(.*?)\\r", texts)
        # for content in text_list:
        # text = content
        # print(text)
        with open('会穿越的道观.txt', 'a') as f:
            for content in text_list:
                text = content
                print(text)
                f.write(text)


get_data()
print('保存完成')
