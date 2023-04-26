import re

import requests


def getUserid(name, q):
    cookies = {
        'sessionid': 'b8f1dd8d52ed015324f4775303146f1a',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        # 'Cookie': 'sessionid=b8f1dd8d52ed015324f4775303146f1a',
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'q': q,
    }

    response = requests.get(
        'http://221.122.54.52:5673/iclock/data/employee/',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )
    html = response.text
    data11 = re.findall(r'data=\[(.*?)];', html, re.S)[0].strip()
    newdata = []
    for i in data11.split('\n'):
        if i:
            newdata.append(eval(i.strip(',')))
    for i in newdata:
            if i[1] == q:
                UserID = i[0]
                # print(f"{name}-{q}: {UserID}")
                return UserID


if __name__ == '__main__':
    data = [
        ['任海军', '7141'],
        ['隗功强', '69540']
    ]
    for n, q in data:
        getUserid(n, q)
