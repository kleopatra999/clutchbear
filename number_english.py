#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-02 13:20:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

zero_nine = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
ten_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_ninety = ['twenty', 'thirty', 'forty', 'fifty',
                 'sixty', 'seventy', 'eighty', 'ninety']


number = int(raw_input('input a number:').strip())

print number, 'is',

if 100 < number < 1000:
    print zero_nine[number / 100], 'hundred and',
number = number - (number / 100) * 100

if 20 <= number <= 99:
    print twenty_ninety[number / 10 - 2] + ' -',

number = number - (number / 10) * 10

if 9 < number < 20:
    print ten_nineteen[number - 10],

if number <= 9:
    print zero_nine[number],
