#-*- coding: utf-8 -*-

#import library
import codecs
import genFormat
import learn
import numpy as np

genFormat.main()
y = np.array(genFormat.y)
#X = model.tranformVector(genFormat.X)
source = np.array(genFormat.source)
X_new = np.hstack((genFormat.X,source))
X = learn.tranformVector(X_new)
#model.train(X_new,y)
learn.crossValidation(X,y)

print "end"
