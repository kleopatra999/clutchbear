#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-09 20:27:52
# @Author  : Xin(skywater@gmail.com)
# @Link    : playbear.github.io

f = open('sina.txt')
data = {}
for line in f.readlines():
    line = line.strip().split()
    data[line[0]] = line[1:]
f.close()
# print data


while True:
    print "========"
    print 'please choice:'
    print '(P)rint'
    print '(F)ind'
    print '(D)el'
    print '(A)dd'
    print '(Q)uit'
    print '========'
    choice = raw_input().strip().lower()
    if len(choice) == 0:
        continue
    elif choice == 'q' or choice == 'quit':
        break
    elif choice == 'p' or choice == 'print':
        for k, v in data.items():
            print '%-25s' % k,
            for i in v:
                print '%-25s' % i,
            print
    elif choice == 'f' or choice == 'find':
        while True:
            print "what you want to find(Q to menu)?"
            find = raw_input().strip().lower()
            if len(find) == 0:
                continue
            elif find == 'q':
                break
            else:
                flag = 0
                for i in data.keys():
                    if find in i:
                        print "%-25s" % i,
                        for k in data[i]:
                            print "%-25s" % k,
                        print
                        flag = 1
                if flag == 0:
                    print 'table have no this one'
    elif choice == 'd' or choice == 'del':
        while True:
            print 'which one your want to del(Q to menu)?'
            delete = raw_input().strip().lower()
            if len(delete) == 0:
                continue
            elif delete == 'q':
                break
            else:
                flag = 0
                for i in data.keys():
                    if delete == i:
                        data.pop(i)
                        print "%s was delete" % i
                        flag = 1
                if flag == 0:
                    print 'table have no this one'
    elif choice == 'a' or choice == 'add':
        print "add items(Q to menu)"
        add = []
        flag = 1
        while flag == 1:
            print "your name:"
            name = raw_input()
            if len(name) == 0:
                continue
            elif name == 'q':
                break
            if name in data.keys():
                print "%s is have" % name
                continue

            print "your phone number:"
            phone = raw_input()
            if len(phone) == 0:
                continue
            elif phone == 'q':
                break
            else:
                add.append(phone)

            print "your email:"
            email = raw_input()
            if len(email) == 0:
                continue
            elif email == 'q':
                break
            else:
                add.append(email)

            print "your department:"
            work = raw_input()
            if len(work) == 0:
                continue
            elif work == 'q':
                break
            else:
                add.append(work)

            data[name] = add
            flag = 0
    else:
        print "wrong choice"
        continue


f = open('sina.txt', 'w+')
data_list = []
for k, v in data.items():
    data_list.append(k +' ' + ' '.join(v))
for i in data_list:
    f.write(i + '\n')
f.close()
