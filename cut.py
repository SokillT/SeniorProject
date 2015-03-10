#-*- coding: utf-8 -*-
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()

f = open('eng.txt','r')
cut = open('3-announce.txt.cut','w')
dic = {}
new = ""	
num = 0

#stopword List
stopwordFile = open('stopword.txt','r')
stopwordLine = stopwordFile.readline()
stopwordLine = stopwordLine.strip()
stopword = stopwordLine.split(' ')

#not use now
charFile = open('alphabet.txt','r')
charLine = charFile.readline()
charLine = charLine.strip()
chars = charLine.split(' ')

s = ["{","}","[","]","#","$","&",".","*",",",";","\\","!",":","?","~","(",")",">","<","/","\'","^","-","@","0","1","2","3","4","5","6","7","8","9"]

for i in f:
	i = i.strip()
 	i = i.replace('\n', '')
	if num >100:
		break
	num += 1
	print num
	if num >100:
		break
	for c in i:
		if (c in s) or c.isalpha():
			new += " "
		else :
			new += c
	fd = new.decode('utf-8')
	result = myKUCut.tokenize([fd])
	for i in result:
		for j in i:
			for k in j:
				word = k.encode('utf-8').lower()
				if (word not in stopword) and word != "":
					if word in dic:
						dic[word] += 1
					else:
						dic[word] = 1
				
print "//////////////////////////////////"
s = sorted(dic.keys())
for key in s:
	print key + " : "+str(dic[key])
	cut.write(key + " : " + str(dic[key])+ "\n")

print len(dic)
