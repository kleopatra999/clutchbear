#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = [['lucy', '25', 'beijing'], ['lilei', '32', 'hongkong'],
       ['hanmeimei', '9', 'sichuan'], ['tom', '13', 'shanghai']]


def age(i):
    return int(i[1])

for i in lst:
    print age(i)

lst.sort(key=age)

print lst
