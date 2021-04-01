import os
import random
import time
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/89.0.4389.90 Safari/537.36",
    "cookie": "UM_distinctid=1785a4cc9f7303-069f2552a41de7-5771031-144000-1785a4cc9f856b",
    "upgrade-insecure-requests": "1"
}


# 获取页面信息
def get_html(url):
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        print("text状态：", response.raise_for_status)
        res = response.content.decode('utf-8')
        return etree.HTML(res)

    except Exception as result:
        print("错误原因0：", result)
        return ''


# 获取单词
def get_words(res):
    words_list = res.xpath('//*[@id="word_list_1"]/li/div[1]/span/text()')
    words_list1 = res.xpath('//*[@id="word_list_2"]/li/div[1]/span/text()')
    # print(words_list)
    new_word_list = []
    for word in words_list:
        word = word.replace('\r', '').replace('\n', '').replace('\t', '')
        new_word_list.append(word)
    for word1 in words_list1:
        word1 = word1.replace('\r', '').replace('\n', '').replace('\t', '')
        new_word_list.append(word1)
    return new_word_list


# 获取音标
def get_phonetic_symbol(res):
    phonetic_symbol_list = res.xpath('//*[@id="word_list_1"]/li/div[2]/strong/text()')
    phonetic_symbol_list1 = res.xpath('//*[@id="word_list_2"]/li/div[2]/strong/text()')
    new_phonetic_symbol_list = []
    for phonetic_symbol in phonetic_symbol_list:
        phonetic_symbol = phonetic_symbol.replace('\r', '').replace('\n', '').replace('\t', '').replace('   ', '')
        new_phonetic_symbol_list.append(phonetic_symbol)
    for phonetic_symbol1 in phonetic_symbol_list1:
        phonetic_symbol1 = phonetic_symbol1.replace('\r', '').replace('\n', '').replace('\t', '').replace('   ', '')
        new_phonetic_symbol_list.append(phonetic_symbol1)
    return new_phonetic_symbol_list


# 获取单词的意思
def get_translate(res):
    translate_list = res.xpath('//*[@id="word_list_1"]/li/div[3]/span/text()')
    translate_list1 = res.xpath('//*[@id="word_list_2"]/li/div[3]/span/text()')
    new_translate_list = []
    for translate in translate_list:
        translate = translate.replace('\r', '').replace('\n', '').replace('\t', '')
        new_translate_list.append(translate)
    for translate1 in translate_list1:
        translate1 = translate1.replace('\r', '').replace('\n', '').replace('\t', '')
        new_translate_list.append(translate1)
    return new_translate_list


# 保存到本地
def save_words(words, phonetic_symbol, translate):
    for i in range(0, 20):
        path = 'English/'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + 'Words.csv', 'a+', encoding='utf-8') as f:
            f.write(words[i] + ',')
            f.write(phonetic_symbol[i] + ',')
            f.write(translate[i])
            f.write('\n')
    print('complete !')


# 运行函数
def run_main():
    for i in range(1, 275):
        print(f"正在爬取第{i}个单词网页")
        url = f'http://word.iciba.com/?action=words&class=13&course={i}'
        text = get_html(url)
        time.sleep(random.uniform(0.1, 1.2))
        word_list = get_words(text)
        phonetic_symbol_list = get_phonetic_symbol(text)
        translate_list = get_translate(text)
        save_words(word_list, phonetic_symbol_list, translate_list)
    print('所有单词保存完成！')


if __name__ == '__main__':
    run_main()
