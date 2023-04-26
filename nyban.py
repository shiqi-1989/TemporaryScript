import re
from pprint import pprint

import requests

cookies = {
    'PHPSESSID': 'sjqp3ecv08gdmk5nnqpfkccr46',
    '__51uvsct__JouBZRmwMTgHCv1D': '1',
    '__51vcke__JouBZRmwMTgHCv1D': '991dbe26-927b-5400-bcc5-36e6335b9e11',
    '__51vuft__JouBZRmwMTgHCv1D': '1676689309371',
    'Hm_lvt_cd7ec7bde4ef8a6a0afaa5a6bc70d921': '1676689309',
    'FF_Cookie': '%7Bvideo%3A%5B%7B%22vodname%22%3A%22%u72C2%u98D9%22%2C%22vodlink%22%3A%22/DaLu/kuangbiao/%22%2C%22cidname%22%3A%22%22%2C%22vodpic%22%3A%22%22%7D%5D%7D',
    '__vtins__JouBZRmwMTgHCv1D': '%7B%22sid%22%3A%20%22ff86795b-8626-596f-ad33-1af6ce64c56a%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%201386822%2C%20%22dr%22%3A%20383649%2C%20%22expires%22%3A%201676692496189%2C%20%22ct%22%3A%201676690696189%7D',
    'Hm_lpvt_cd7ec7bde4ef8a6a0afaa5a6bc70d921': '1676690696',
}

headers = {
    'authority': 'www.quanji55.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=sjqp3ecv08gdmk5nnqpfkccr46; __51uvsct__JouBZRmwMTgHCv1D=1; __51vcke__JouBZRmwMTgHCv1D=991dbe26-927b-5400-bcc5-36e6335b9e11; __51vuft__JouBZRmwMTgHCv1D=1676689309371; Hm_lvt_cd7ec7bde4ef8a6a0afaa5a6bc70d921=1676689309; FF_Cookie=%7Bvideo%3A%5B%7B%22vodname%22%3A%22%u72C2%u98D9%22%2C%22vodlink%22%3A%22/DaLu/kuangbiao/%22%2C%22cidname%22%3A%22%22%2C%22vodpic%22%3A%22%22%7D%5D%7D; __vtins__JouBZRmwMTgHCv1D=%7B%22sid%22%3A%20%22ff86795b-8626-596f-ad33-1af6ce64c56a%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%201386822%2C%20%22dr%22%3A%20383649%2C%20%22expires%22%3A%201676692496189%2C%20%22ct%22%3A%201676690696189%7D; Hm_lpvt_cd7ec7bde4ef8a6a0afaa5a6bc70d921=1676690696',
    'pragma': 'no-cache',
    'referer': 'https://www.quanji55.net/DaLu/kuangbiao/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    's': 'User-Comm-getcomm-id-133006',
}

response = requests.get('https://www.quanji55.net/DaLu/kuangbiao/')
html = response.text
url_list = re.findall(r'class="down_url" value="(.*?)"', html, re.S)
for i in url_list:
    print(i)