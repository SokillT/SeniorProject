#-*- coding: utf-8 -*-
import codecs
import re
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()

f = open('topic_nisit_sample.txt','r')
cut = open('topic_nisit_sample.txt.cut','w')
dic = {}
new = ""	
num = 0
for i in f:
	i = i.strip()
	i = i.replace('\n', '')
	num += 1
	print num
	for c in i:
		m = re.match("\d",c)
		if m:
			new += " "
		elif c in "{}[]#$&.*,;\"\n!:?~()></\\'^":
			new += " "
		else :
			new += c
	fd = new.decode('utf-8')
	result = myKUCut.tokenize([fd])
	for i in result:
		for j in i:
			for k in j:
				word = k.encode('utf-8')
				#print word
				
				if word in dic:
					dic[word] += 1
				else:
					dic[word] = 1
				
print "//////////////////////////////////"
s = sorted(dic.keys())
for key in s:
	print key + " : "+str(dic[key])
	cut.write(key + " : " + str(dic[key])+ "\n")

#for i,j in s.items():
#	print i.decode('utf-8')+ str(j)
print len(dic)
