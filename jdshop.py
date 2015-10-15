#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-13 19:52:06
import requests
from bs4 import BeautifulSoup

url = 'http://list.jd.com/list.html?cat=9987%2C653%2C655&page=1'

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

items = soup.select('li.gl-item')

# print len(items)

for item in items:
    sku = item.find('div')['data-sku']
    print sku,
    price_url = 'http://p.3.cn/prices/mgets?skuIds=J_' + str(sku)
    price = requests.get(price_url).json()[0]['p']
    print price,
    nameinfo = item.find('div', class_="p-name").find('a')
    name = nameinfo['title']
    item_url = 'http:' + nameinfo['href']
    print name, item_url,
    commit = item.find('div', class_="p-commit").find('a')
    if commit:
        print commit.get_text()
