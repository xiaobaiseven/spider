import requests
url = 'https://www.cenzqxx.com/qingchun'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36',
    'Referer': 'https://www.cenzqxx.com'
}
response = requests.get(url, headers=headers).content.decode('utf-8')
print(response)