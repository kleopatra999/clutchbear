#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-13 08:17:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import datetime


def login(account, lock=[]):
    count = 0
    print "input your password:"
    while True:
        password = raw_input().strip()
        if len(password) == 0:
            continue
        if account_data[account][0] != password:
            print "wrong password, input again"
            count += 1
            if count >= 3:
                lock.append(account)
                with open('lock.txt', 'a+') as f:
                    f.write(account + '\n')
                print "over 3 times worng password, your account was locked"
                return 0
                break
        else:
            print "welcome %s to credit crad sys" % account
            return 1
            break


def loger(account_data={}):
    while True:
        date = datetime.date.today()
        print date
        print """
        which one you choice:
        (C)offee
        (S)hoe shop


        """



def encashment(account, date, type, amount, interest):
    pass

with open('account.txt', 'r') as f:
    account_data = {}
    for line in f.readlines():
        line = line.strip().split()
        account_data[line[0]] = line[1:]

with open('lock.txt', 'r') as f:
    lock = []
    for line in f.readlines():
        lock.append(line.strip())


while True:
    account = raw_input('input your credit card login name:\n').strip()
    if len(account) == 0:
        continue
    if account not in account_data:
        print "wrong credit card name, input again"
        continue
    if account in lock:
        print "your card number was locked, out!"
        break
    if not login(account, lock):
        break

while True:
    print '''
    which one you choice:
    (E)ncashment
    (C)onsume
    (Q)uit
    '''
    choice = raw_input().strip().lower()
    if len(choice) == 0:
        continue
    if choice == 'q' or choice == 'quit':
        break
    if choice == 'e' or choice == 'encashment':
        encashment
    if choice == 'c' or choice == 'consume':
        loger(account_data)



















