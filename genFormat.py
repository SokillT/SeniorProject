#-*- coding: utf-8 -*-

#import library
from kucut import SimpleKucutWrapper as KUCut
import codecs
import math
myKUCut = KUCut()

def setGlobal():
	print "==> setGlobal"
	global stopword
	global dic
	global totaldic
	global X
	global y
	global source
	global train
	global test
	global cut
	#global N 	#Number of doc in collection

def readInput(filename):
	print "==> readInput"
	f = open(filename,'r')
	return f

def readStopword():
	print "==> readStopword"
	stopwordFile = open('stopword.txt','r')
	stopwordLine = stopwordFile.readline()
	stopwordLine = stopwordLine.strip()
	stopword = stopwordLine.split(' ')
	return stopword

def addTotaldic(dic):
	print "==> addTotaldic"
	s=sorted(dic.keys())
	for key in s:
		if dic[key] > 10:
			totaldic.append(key)
			print key + " : " + str(dic[key])
		#cut.write(key + " : " + str(dic[key]) + "\n")
	#print len(totaldic)

def tokenize(title):
	#print "==> tokenize"
	count = 0
	s = ["{","}","[","]","#","$","&",".","*",",",";","\\","!",":","?","~","(",")",">","<","/","\'","^","-","_","@","0","1","2","3","4","5","6","7","8","9"]
	
	new = ""
	for c in title:
		if (c in s) or c.isalpha():
			new += " "
		else :
			new += c
	newword = new.decode('utf-8')
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
						#df[word] = 0

def gen_vector():
	vector = {}
	for i in totaldic:
		vector[i] =0
	return vector

def vectorspace(title,n):
	#print "==> vectorspace"
	# n is class number
	vector = {}
	item = []
	s = ["{","}","[","]","#","$","&",".","*",",",";","\\","!",":","?","~","(",")",">","<","/","\'","^","-","_","@","0","1","2","3","4","5","6","7","8","9"]
	
	new = ""
	for c in title:
		if (c in s) or c.isalpha():
			new += " "
		else :
			new += c
	newword = new.decode('utf-8')
	result = myKUCut.tokenize([newword])
	for i in result:
		for j in i:
			for k in j:
				word = k.encode('utf-8').lower()
				if (word not in stopword) and word != "":
					if word in totaldic:
						if word in vector:
							vector[word] += 1
							print "add"
						else:
							cut.write("," + word)
							vector[word] = 1
							print "1"
	for i in totaldic:
		if i not in vector:
			vector[i] = 0
		else:
			vector[i] = vector[i]

	vectors=sorted(vector.keys())
	for w in vectors:
		item.append(vector[w])
		train.write(str(vector[w]) + ",")
	X.append(item)
	y.append(n)
	train.write("\n")

def main():
	c =0
	count = 0
	for name in listFilename:
		count += 1
		f = readInput(name)
		line = ""
		for line in f:
			details = []
			line = line.strip()
			line = line.replace('\n','')
			split = line.split(',')
			if split[1] != "4" :
				details.append(split[0])
				details.append(split[1])
				details.append(split[2])
				details.append(split[3])
				allNews.append(details)
				if count == 1:
					a = [1,0,0,0]
					source.append(a)
				elif count == 2:
					a = [0,1,0,0]
					source.append(a)
				elif count == 3:
					a = [0,0,1,0]
					source.append(a)
				elif count == 4:
					a = [0,0,0,1]
					source.append(a)
				else:
					c += 1
	for item in allNews:
		try:
			tokenize(item[2])
		except(UnicodeEncodeError):
			print "ERROR!!!" + item[2] +":", item[0]
			pass
	addTotaldic(dic)
	for item in allNews:
		#print item[2]
		cut.write(item[0] +","+item[1])
		vectorspace(item[2],item[1])
		cut.write("\n")
	print len(allNews)

#output file
train = open('train.txt','w')
cut =open('topic_cut.txt','a')

#declar variable & iniatial value
dic = {}
totaldic = []
stopword = []
allNews =[]
X = []
y = []
source = []
setGlobal()	
listFilename = ["2015-04-26 intaff.txt","2015-04-26 ku.txt","2015-04-26 engAnnounce.txt","2015-04-26 nisit.txt"]
readStopword()
