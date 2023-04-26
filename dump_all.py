import re

from requests_toolbelt.utils import dump
import requests
import http


# http.client.HTTPConnection.debuglevel = 1


def logging_hook(response, *args, **kwargs):
    data = dump.dump_all(response)
    print(data)
    con = data.decode('utf-8')
    for n in con.split('\r\n\r\n'):
        print(n)
        #
        # for i in n.splitlines():
        #     print(i)



http = requests.Session()
http.hooks["response"] = [logging_hook]
http.get("https://api.openaq.org/v1/cities", params={"country": "BA"})