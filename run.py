#-*- coding: utf-8 -*-

#import library
import codecs
import genFormat
import model
import numpy as np

genFormat.main()
y = np.array(genFormat.y)
#X = model.tranformVector(genFormat.X)
source = np.array(genFormat.source)
X_new = np.hstack((genFormat.X,source))
X = model.tranformVector(X_new)
#model.train(X_new,y)
model.crossValidation(X,y)

f = codecs.open('X_count.txt','w','utf-8')
for i in X_new:
	f.write(i);

print "yes"
