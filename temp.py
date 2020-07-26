import requests
from lxml import etree
import os
import re
import time

url = 'https://m.nvshens.net/gallery/2.html'  # 此处的url可用https://m.nvshens.net/gallery/{}.html.format(i)来替代,从而实现多页爬取
headers = {
    'Referer':
    'https://m.nvshens.net/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
total_path = 'D:/testpic'
if not os.path.exists(total_path):
    os.makedirs(total_path)
Error = []
response = requests.get(url, headers=headers)
html = response.content.decode()
element = etree.HTML(html)
pages_link = element.xpath('//*[@id="gallerydiv"]/div/div/a//@href')
# print(pages_link)
for page_link in pages_link:
    res = requests.get(page_link, headers=headers)
    page = res.content.decode()
    page_element = etree.HTML(page)
    name = page_element.xpath('//*[@id="htitle"]//text()')[0]
    img_path = 'D:/testpic/{}'.format(name)
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    temp = page_element.xpath('//*[@id="pagediv"]/span[2]//text()')[0]
    page_num = int(re.findall(r'\d*\d', temp)[1])
    # print(ret)
    # https://m.nvshens.net/g/33301/1.html
    imgs_url = []
    for i in range(1, page_num + 1):
        link = page_link + '/' + str(i) + '.html'
        link_res = requests.get(link, headers=headers)
        link_html = link_res.content.decode()
        link_element = etree.HTML(link_html)
        temp_url = link_element.xpath('//*[@id="idiv"]/div/img//@src')
        imgs_url += temp_url
    # print(imgs_url)
    for img_url in imgs_url:
        img = requests.get(img_url, headers=headers)
        img_name = str(int(time.time() * 100))
        path = 'D:/testpic/{}/{}.jpg'.format(name, img_name)
        try:
            with open(path, 'wb') as f:
                f.write(img.content)
        except Exception:
            Error.append(img_url)
    time.sleep(0.2)
    print(name + ' 已完成')
print(Error)
