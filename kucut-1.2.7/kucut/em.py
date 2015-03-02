#!/usr/bin/python

from wordcut import *
	
def simple_cut_all(self,lines,output_file):
	fout = open(output_file,'w')
	for line in lines:
		tokens = line.split()
		for token in tokens:
			self.setLine(token)
			results = self.docut(filter=False)[0]
			for result in results:					
				fout.write('%s\n' % (result))
			fout.write('\n')
	fout.close()	
	
def resegment(self,corpus_file,input_file,output_file,n):
	fout = open(output_file,'w')

	ngram_model = AIMA.text.NgramTextModel(n=n,default=1)
	for line in open(corpus_file).readlines():
		words = line.split()
		ngram_model.add_sequence(words)

	lines = open(input_file).readlines()
	for line in lines:
		tokens = line.split()
		for token in tokens:
			self.setLine(token)
			results = self.docut(filter=False)[0]
			tmp = []
			for result in results:
				cost = 1
				words = ['',]*(n-1)+result.split()
				for i in range(len(words)-n):
					cost = cost * ngram_model[tuple(words[i:i+n])]
				tmp.append((cost,result))
			x,y = max(tmp)
			print x,y
			fout.write('%s\n' % (min(tmp)[1]))
	fout.close()
	
def check_cost(self,corpus_file):
	unigram_model = AIMA.text.UnigramTextModel(default=1)
	total = 0
	for token in open(corpus_file).read().split():
		total += 1
		unigram_model.add(token)
		
	cost = 0
	for token in open(corpus_file).read().split():
		cost += (-math.log(unigram_model[token]))/float(total)
	return cost,total

if __name__ == '__main__':
	syldict = Dictionary('dict/syllable.txt')
	lexdict = Dictionary('dict/lexicon.txt')
	segmentor = Segmentation(syllable=syldict,lexicon=lexdict)
	segmentor.resegment('test_em.random.cut','test_em.txt','test_em.01.cut',2)
