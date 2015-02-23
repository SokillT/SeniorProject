# -*- coding: utf-8 -*-
import codecs
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()

f = open('topic.txt','r')
for i in f:
	i = i.strip()
	i = i.replace('\n', '')
	fd = i.decode('utf-8')
	result = myKUCut.tokenize([fd])
	for i in result:
		for j in i:
			for k in j:
				print k.encode('utf-8')

