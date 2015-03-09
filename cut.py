#-*- coding: utf-8 -*-
import codecs
import re
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()

f = open('topic_ku.txt','r')
cut = open('topic_ku.txt.cut','w')
dic = {}
new = ""	
num = 0

#stopword List
stopwordFile = open('stopword.txt','r')
stopwordLine = stopwordFile.readline()
stopwordLine = stopwordLine.strip()
stopword = stopwordLine.split(' ')

charFile = open('alphabet.txt','r')
charLine = charFile.readline()
charLine = charLine.strip()
chars = charLine.split(' ')

for i in f:
	i = i.strip()
	i = i.replace('\n', '')
	num += 1
	print num
	for c in i:
		if (c in chars) or c.isalpha():
			new += c
		#elif c in "{}[]#$&.*,;\"\n!:?~()></\\'^":
		#	new += " "
		else :
			new += " "
	fd = new.decode('utf-8')
	result = myKUCut.tokenize([fd])
	for i in result:
		for j in i:
			for k in j:
				word = k.encode('utf-8').lower()
				#print word
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
