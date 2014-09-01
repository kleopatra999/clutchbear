with open('emma.txt', 'r') as f:
	count = {}
	for line in f:
		line = line.strip()
		#print line
		words = line.split()
		#print words
		for word in words:
			#print word,
			if word in count:
				count[word] +=1
			else:
				count[word] = 1

	#print count.keys()
	num = []
	for k, v in count.items():
		num.append([v, k])

	num.sort(reverse =True )
	#print num
	for i in num[:10]:
		print i[1],i[0]


