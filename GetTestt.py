import requests

from Html_test import getUserid


def kaoqin(name, q):
    cookies = {
        'sessionid': 'b8f1dd8d52ed015324f4775303146f1a',
    }

    headers = {
        'Host': '221.122.54.52:5673',
        'Accept': 'text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Origin': 'http://221.122.54.52:5673',
        'Referer': 'http://221.122.54.52:5673/iclock/data/employee/?q=69777',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'sessionid=b8f1dd8d52ed015324f4775303146f1a',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    UserID = getUserid(name, q)
    if UserID:
        print(f"{name}-{q}: {UserID}")

        for sn in ['3389152900267',
                   '3389152900262',
                   '3389152900265',
                   '3389152900261',
                   '6572173700223']:
            params = {
                'q': q,
                'action': 'toDev',
                'SN': sn,
            }

            data = f'&K={UserID}'
            try:
                response = requests.post(
                    'http://221.122.54.52:5673/iclock/data/employee/',
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                )
                print(f"{response.status_code}:{response.text};{q}|{sn}:成功")
            except:
                print(f"{q}|{sn}:失败")
    else:
        print(f"{name}-{q}: 账号不存在！")


if __name__ == '__main__':
    # kaoqinData = get_xls('石延磊')
    kaoqinData = [
        ['任海军', '7141'],
        ['隗功强', '69540']
    ]
    num = 0
    for name, q in kaoqinData:
        kaoqin(name, q)
        num += 1
    print(f"执行：{num}")
