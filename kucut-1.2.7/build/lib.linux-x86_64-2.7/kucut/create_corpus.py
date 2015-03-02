#!/usr/bin/python

import sys, time
import AIMA.text

if len(sys.argv) != 3:
	sys.__stderr__.write('Usage: %s input_file output_file\n' % (sys.argv[0]))
	sys.exit(1)
	
input_file = sys.argv[1]

lines = open(input_file).readlines()

print 'start %s' % (time.ctime())

unigram = AIMA.text.UnigramTextModel(default=1)
bigram = AIMA.text.UnigramTextModel(default=1)
trigram = AIMA.text.UnigramTextModel(default=1)

unigram_keys = ['<-default->']
bigram_keys = ['<-default->']
trigram_keys = ['<-default->']

CAT = lambda x,y : x + ' ' + y
for line in lines:
	words = line.split()
	for i in range(len(words)):
		unigram.add(words[i])
		if words[i] not in unigram_keys:
			unigram_keys.append(words[i])
		if i > 0:
			x = reduce(CAT,words[i-1:i+1])
			bigram.add(x)
			if x not in bigram_keys:
				bigram_keys.append(x)
		if i > 1:
			x = reduce(CAT,words[i-2:i+1])
			trigram.add(x)
			if x not in trigram_keys:
				trigram_keys.append(x)

unigram.add('<-default->')
bigram.add('<-default->')
trigram.add('<-default->')

output = open(output_file,'w')

for key in unigram_keys:
	output.write('%s %s\n'%(key,str(unigram[key])))
for key in bigram_keys:
	output.write('%s %s\n'%(key,str(bigram[key])))
for key in trigram_keys:
	output.write('%s %s\n'%(key,str(trigram[key])))

output.close()

print 'finish %s'%(time.ctime())
