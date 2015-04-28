from sklearn import svm										# svm classification	
from sklearn import cross_validation
from sklearn.cross_validation import StratifiedKFold			# cross validation
from sklearn.feature_extraction.text import TfidfTransformer	# tranform value from count to tf-idf
from sklearn.externals import joblib							# help to save model					
from sklearn.metrics import accuracy_score						# calculate accuracy
from sklearn.metrics import classification_report				# evaluation
import numpy as np

#not
def crossValidation(X,y):
	target_names = ['class 1', 'class 2', 'class 3', 'class 4']

	cross = open('report2.txt','w')
	#scores = cross_validation.cross_val_score(clf,X,y,10)
	skf = StratifiedKFold(y, 10)
	i = 0
	sum = 0
	for train_index, test_index in skf:
		i+= 1
		#print("TRAIN:", train_index, "TEST:", test_index)
		X_train, X_test = X[train_index], X[test_index]
		y_train, y_test = y[train_index], y[test_index]
		train(X_train,y_train,i)
		y_pred = predict(X_test,i)

		print "NUMBER OF TEST : " + str(i)
		print classification_report(y_test, y_pred, target_names=target_names)
		cross.write(classification_report(y_test, y_pred, target_names=target_names))
		cross.write("\n")

		'''
		accuracyValue = accuracy_score(y_test, y_pre)
		sum += accuracyValue
		print accuracyValue
		cross.write("y_pre : \n")
		for j in y_pre:
			cross.write(str(j) + " ")
		cross.write("\n")
		cross.write("y_true : \n")
		for j in y_test:
			cross.write(str(j) + " ")
		cross.write("\n")
		cross.write("accuracyValue : " +str(accuracyValue)+ "\n")
	cross.write("accuracyAverage : " +str(sum/10)+ "\n")

	print "accuracyAverage : " +str(sum/10)
	'''

def tranformVector(X):
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(X)
	return tfidf.toarray()         

def train(X,y,i):
	#X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
	#y = np.array([1, 1, 2, 2])
	clf = svm.SVC()
	clf.fit(X, y)
	name = "svmModel" + str(i) + ".pkl"
	joblib.dump(clf, name)

def predict(X_test,i):
	name = "svmModel" + str(i) + ".pkl"
	clf2 = joblib.load(name)
	y_pre =clf2.predict(X_test)
	return y_pre