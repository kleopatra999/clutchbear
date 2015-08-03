#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import time
import codecs

keyfile = open('keyword.txt')
for keyWord in keyfile.read().lower().strip().split():
    if keyWord.isalpha():
        print keyWord
        f = codecs.open('%s_result.txt' % keyWord, 'wb', 'utf-8')

        url = 'http://www.iciba.com/' + keyWord

        my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
                      'Host': 'www.iciba.com',
                      }
        time.sleep(1)
        req = urllib2.Request(url, headers=my_headers)
        response = urllib2.urlopen(req)
        html = response.read()

        soup = BeautifulSoup(html, "html.parser")
        word = soup.find('h1', id="word_name_h1")

        f.write(u'【关键字】 ')
        f.write(word.get_text())

        yinbiaos = soup.find_all('span', class_='eg')
        f.write('\n')
        f.write(u'【音标】')
        for yinbiao in yinbiaos:
            f.write(' '.join(yinbiao.get_text().strip().split()) + ' ')

        f.write('\n')
        f.write(u'【解释信息】' + '\n')
        jieshi = soup.find('div', class_='group_pos')
        for i in range(1, len(jieshi.contents), 2):
            f.write("".join(jieshi.contents[i].get_text().strip().split()) + '\n')

        f.write(u'【网络释义】' + '\n')
        net = soup.find('ul', class_='clear')
        f.write(''.join(net.get_text().split()))

        f.write('\n')
        f.write(u'【词性变换】' + '\n')
        fushus = soup.find_all('div', class_='group_inf')
        for item in fushus:
            if item.get('style') == 'background:#f7f7f7;':
                f.write(u'无')
                continue
            else:
                f.write(' '.join(item.get_text().strip().split()))
