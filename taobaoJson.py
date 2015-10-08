#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-08 01:33:29
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
from pprint import pprint
# 淘宝搜索商品json链接
url = 'https://s.taobao.com/search?data-key=s&data-value=132&ajax=true&_ksTS=1444303966469_1084&spm=a21bo.7724922.8452-sline.3.LX6mTf&q=%E5%86%B2%E9%94%8B%E8%A1%A3&refpid=430268_1006&source=tbsy&style=grid&tab=all&pvid=5d9ef5842a91964bfbf7cddc70c7ae5b&bcoffset=-2&p4poffset=4&s=88'

req = requests.get(url)

# pprint(req.json())
# 页数信息,
page = req.json()['mods']['pager']['data']
print page

shop = req.json()['mods']['itemlist']['data']['auctions']


for item in shop:
    print item['raw_title'].encode('utf-8'), item['detail_url'].encode('utf-8')
