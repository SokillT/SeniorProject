# -*- coding: utf-8 -*-
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()
#result = myKUCut.tokenize([u"ทดสอบทดสอบ"])
#print u"\n".join([u"\n".join([u" ".join([w for w in line])for line in p])for p in result])

w = "ทดสอบทดสอบ"
we = w.decode('utf-8')
result = myKUCut.tokenize([we])
for i in result:
	for j in i:
		for k in j:
			print k.encode('utf-8')
print result
