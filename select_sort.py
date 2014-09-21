arry = [11, 10, 7, 3, 10003,3, 4,450 6, 9, 5, 4, 100, 112]

for i in range(len(arry) - 1):
	flag = i
	for j in range(i, len(arry)):
		if arry[j] < arry[flag]:
			flag = j
	arry[flag],arry[i] = arry[i], arry[flag]
	print j, i
	print arry

print arry
