from urllib import parse
ddc = {
    "aa": 11,
    "bb": "11"
}
print(parse.urlencode(ddc))