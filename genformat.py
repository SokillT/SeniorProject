#-*- coding: utf-8 -*-

#import library
from kucut import SimpleKucutWrapper as KUCut
import math
myKUCut = KUCut()

def set_globalvar():
	print "==> set_globalvar"
	global stopword
	global s
	global dic
	global df
	global idf
	global weight
	global totaldic
	global train
	global test
	#global N 	#Number of doc in collection

def inputfile(filename):
	print "==> inputfile"
	f = open(filename,'r')
	return f

def stopwordfile():
	print "==> stopwordfile"
	stopwordFile = open('stopword.txt','r')
	stopwordLine = stopwordFile.readline()
	stopwordLine = stopwordLine.strip()
	stopword = stopwordLine.split(' ')
	return stopword

def printdic(dic):
	print "==> printdic"
	s=sorted(dic.keys())
	for key in s:
		if dic[key] > 10:
			totaldic.append(key)
			print key + " : " + str(dic[key])
		#cut.write(key + " : " + str(dic[key]) + "\n")
	print len(totaldic)

def tokenize(filename):
	print "==> tokenize"
	count = 0
	s = ["{","}","[","]","#","$","&",".","*",",",";","\\","!",":","?","~","(",")",">","<","/","\'","^","-","@","0","1","2","3","4","5","6","7","8","9"]
	newword = ""
	listword = [] #list of word in each doc

	for line in f:
		line = line.strip()
		line = line.replace('\n','')
		count += 1
		if count > 100:
			break
		print count
		newword = line.decode('utf-8')
		result = myKUCut.tokenize([newword])
		for i in result:
			for j in i:
				for k in j:
					word = k.encode('utf-8').lower()
					if (word not in stopword) and word != "":
						if word in dic:
							dic[word] += 1
						else:
							dic[word] = 1
							df[word] = 0
						if word not in listword:
							listword.append(word) 
	for i in listword:
		df[i] += 1
	return count

def gen_vector(dic):
	vector = {}
	for i in totaldic:
		vector.update({i:0})
	return vector

def vectorspace(line,n):
	vector = {}
	#print "==> vector"
	#vector = gen_vector(dic)
	#for i in vector:
	#	print i + str(vector[i])
	newword = ""
	newword = line.decode('utf-8')
	result = myKUCut.tokenize([newword])
	for i in result:
		for j in i:
			for k in j:
				word = k.encode('utf-8').lower()
				if (word not in stopword) and word != "":
					if word in totaldic:
						if word in vector:
							vector[word] += 1
						else:
							vector[word] = 1
	for i in totaldic:
		if i not in vector:
			vector[i] = 0
		else:
			vector[i] = vector[i]*idf[i]

	vectors=sorted(vector.keys())
	index = 1
	if n!= 4:
		train.write(str(n))
		for w in vectors:
			train.write(" "+str(index)+":"+str(vector[w]))
			index += 1
		train.write("\n")
	else:
		test.write("x")
		for w in vectors:
			test.write(" "+str(index)+":"+str(vector[w]))
			index += 1
		test.write("\n")

def idfCal():
	for i in totaldic:
		idf[i] = math.log((N/df[i]),10)

#output file
train = open('train.txt','w')
test = open('test.txt','w')

#declar variable & iniatial value
dic = {}
df = {}
idf = {}
weight = {}
totaldic = []
stopword = []
N = 0
set_globalvar()
List_filename = ["1-scholarship.txt","2-activity.txt","eng.txt","raw_test2.txt"]
stopwordfile()

#main
for name in List_filename:
	f = inputfile(name)
	N += tokenize(f)

#show dic
printdic(dic)
idfCal()

n=0
for name in List_filename:
	f = inputfile(name)
	n += 1
	for line in f:
		line = line.strip()
		line = line.replace('\n','')
		vectorspace(line,n)	

print "N = " + str(N)