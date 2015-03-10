#-*- coding: utf-8 -*-

#import library
from kucut import SimpleKucutWrapper as KUCut
myKUCut = KUCut()

def set_globalvar():
	print "==> set_globalvar"
	global stopword
	global s
	global dic
	global totaldic
	global train
	global test

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

	for line in f:
		line = line.strip()
		line = line.replace('\n','')
		count += 1
		print line
		#if count > 100:
		#	break
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

	vectors=sorted(vector.keys())
	train.write(str(n))
	index = 1
	for w in vectors:
		train.write(" "+str(index)+":"+str(vector[w]))
		index += 1
	train.write("\n")

#output file
train = open('train.txt.cut','w')
test = open('test.txt.cut','w')

#declar variable & iniatial value
dic = {}
totaldic = []
stopword = []
set_globalvar()
List_filename = ["1-scholarship.txt","2-activity.txt","eng.txt"]
stopwordfile()

#main
for name in List_filename:
	f = inputfile(name)
	tokenize(f)

#show dic
printdic(dic)

n=0
for name in List_filename:
	f = inputfile(name)
	n += 1
	for line in f:
		line = line.strip()
		line = line.replace('\n','')
		vectorspace(line,n)





	
	