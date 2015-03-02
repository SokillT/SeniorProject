#!/usr/bin/python

import wordcut
import sys, dbhash, math
from wordcut import Dictionary

class MutualInformation:
	def __init__(self):
		self.mem = {}

	def create_mem(self,filename):
		db = {}
		lines = map(str.strip,open(filename).readlines())
		unigram = 0
		bigram = 0
		for line in lines:
			tokens = line.split()
			key = []
			for token in tokens:
				unigram += 1
				if token in db:
					db[token] = str(int(db[token]) + 1)
				else:
					db[token] = '1'

				key.append(token)
				if len(key) == 2:
					s_key = key[0]+' '+key[1]
					bigram += 1
					if s_key in db:
						db[s_key] = str(int(db[s_key]) + 1)
					else:
						db[s_key] = '1'
					del key[0]
		db['unigrams'] = str(unigram)
		db['bigrams'] = str(bigram)
		
		self.mem = db.copy()
	
	def create_db(self,filename,dbname):
		db = dbhash.open(dbname,'w')
		lines = map(str.strip,open(filename).readlines())
		unigram = 0
		bigram = 0
		for line in lines:
			tokens = line.split()
			key = []
			for token in tokens:
				unigram += 1
				if token in db:
					db[token] = str(int(db[token]) + 1)
				else:
					db[token] = '1'

				key.append(token)
				if len(key) == 2:
					s_key = key[0]+' '+key[1]
					bigram += 1
					if s_key in db:
						db[s_key] = str(int(db[s_key]) + 1)
					else:
						db[s_key] = '1'
					del key[0]
		db['unigrams'] = str(unigram)
		db['bigrams'] = str(bigram)
		db.close()
		
	def get_cost(self,x,y,dbname=None):
		db = None
		if dbname != None:
			db = dbhash.open(dbname)
		else:
			db = self.mem.copy()
		if db == None:
			return 0
		bi_key = x+' '+y
		try:
			p_xy = float(db[bi_key].split()[0])/int(db['unigrams'])
		except KeyError,e:
			p_xy = 0.0000000001
		try:
			p_x = float(db[x])/int(db['unigrams'])
		except KeyError,e:
			p_x = 0.0000000001
		try:
			p_y = float(db[y])/int(db['unigrams'])
		except KeyError,e:
			p_y = 0.0000000001

		if dbname != None:
			db.close()

		mi = p_xy/(p_x * p_y)
		return math.log(mi)

class UnknownWordDetector:
	def __init__(self,filename,lexicon):
		self.lines = map(str.strip,open(filename).readlines())
		self.lexicon = wordcut.Dictionary(lexicon)
		self.unknown_list = []
	
	def compute(self):
		tmp = {}
		for line in self.lines:
			tokens = line.split()
			i = 0
			for token in tokens:
				if not self.lexicon.contains(token) and token not in self.unknown_list and wordcut.Segmentation.IsThaiWord(token):
					if token not in tmp:
						tmp[token] = (1,[])
					else:
						value,context = tmp[token]
						value += 1
						tmp[token] = (value,context)

					ls,rs = '',''
					if i > 2 and i < len(tokens) - 2:
						ls = '%s %s' % (tokens[i-2],tokens[i-1])
						rs = '%s %s' % (tokens[i+1],tokens[i+2])
					elif i > 1 and i < len(tokens) - 2:
						ls = '%s' % (tokens[i-1])
						rs = '%s %s' % (tokens[i+1],tokens[i+2])									 
					elif i > 2 and i < len(tokens) - 1:
						ls = '%s %s' % (tokens[i-2],tokens[i-1])
						rs = '%s' % (tokens[i+1])
					elif i > 1 and i < len(tokens) - 1:
						ls = '%s' % (tokens[i-1])
						rs = '%s' % (tokens[i+1])
					elif i < len(tokens) - 1:
						rs = '%s' % (tokens[i+1])
					elif i > 1:
						ls = '%s' % (tokens[i-1])						

					if (ls,rs) not in tmp[token][1]:
						tmp[token][1].append((ls,rs))
				i += 1

		return tmp.copy()
	
def IsIntersect(s1,s2):
	for i in s1:
		if i in s2:
			return True
	return False

def IsSubset(s1,s2):
	for i in s1:
		if i not in s2:
			return False
	return True
				
if __name__ == '__main__':
#	'VCS VEX VI VPOST VT ADV ADVM1 ADVM2 ADVM3 ADVM4'
#	pos = 'ADJ ADJBE NCN NPN'.split()
#	lexicon = Dictionary('pos.txt')
#	mi = MutualInformation()
#	lines = open('bkknews.txt.cut')
#	tmp = []
#	for line in map(str.strip,lines):
#		tokens = line.split()
#		for i in range(len(tokens))[1:]:
#			if not wordcut.Segmentation.IsThaiWord(tokens[i-1]) or not wordcut.Segmentation.IsThaiWord(tokens[i]):
#				continue
#			if IsSubset(lexicon.gettag(tokens[i-1]),pos) and IsSubset(lexicon.gettag(tokens[i]),pos):
#				print tokens[i-1],tokens[i]
#				print lexicon.gettag(tokens[i-1]),lexicon.gettag(tokens[i])
#				local_mi = mi.get_cost(tokens[i-1],tokens[i],'bkknews.db')
#				global_mi = mi.get_cost(tokens[i-1],tokens[i],'corpus.db')
#				if local_mi > 1 and global_mi > 0 and local_mi / global_mi > 1:	
#					x = '%s %s' % (tokens[i-1],tokens[i])
#					if x not in tmp:
#						tmp.append(x)
#	for t in tmp:
#		print t
#	print mi.get_cost('การ','เมือง','corpus.db')
#	print mi.get_cost('การ','เมือง','large-test.db')
#	mi.create_db('bkknews.txt.cut','bkknews.db')
	
	lexicon = sys.argv[1]
	filename = sys.argv[2]
	
	uwd = UnknownWordDetector(filename,lexicon)
	result = uwd.compute()
	tmp = []
	for key in result.keys():
		tmp.append((result[key][0],key))
	tmp.sort()
	tmp.reverse()
	for t in tmp:
		print t[1],t[0]
