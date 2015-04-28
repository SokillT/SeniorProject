#-*- coding: utf-8 -*-

#import library
import codecs

an330=[]
sql = ""

check = codecs.open('check.txt','r','utf-8')
f = codecs.open('topic_cut.txt','r','utf-8')
s = codecs.open('sql.txt','w','utf-8')
for line in f:
	line = line.strip('\n')
	a = line.split(',')
	for i in a :
		b= check.readline()
		b=b.strip('\n')
		if a[1] == "3":
			test = int(a[0])
			if test not in an330:
				an330.append(test)
				print test
print len(an330)

for i in an330:
	s.write(sql+";\n") 
	sql = "INSERT INTO `news_news2sub`(`Nid_id`, `Sid_id`) VALUES ("+str(i)+",330);"