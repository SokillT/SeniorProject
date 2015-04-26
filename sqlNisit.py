# -*- coding: utf-8 -*- 
import codecs

f = codecs.open('nisit.txt','r','utf-8')
for line in f:
	details = line.split(',')
	print details