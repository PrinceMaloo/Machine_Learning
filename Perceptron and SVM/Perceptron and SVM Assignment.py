# -*- coding: utf-8 -*-
"""Lab9_B21CH025

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9lduj0PiZCyIjp9d-SjEZbZX43L7IaH

Part A question 1
"""

import numpy as np
import pandas as pd
from sklearn import linear_model, svm
from sklearn import datasets

from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/IML Lab/data_banknote_authentication.txt', names = [ 'variance of Wavelet Transformed image (continuous)', 'skewness of Wavelet Transformed image (continuous)', 'curtosis of Wavelet Transformed image (continuous)', 'entropy of image (continuous)', 'class (integer)'])

df

df.describe()

df.head()

df.info()

X = df.drop(columns=['class (integer)'])
Y = df['class (integer)']

from sklearn.model_selection import train_test_split
X_train, X_rem, Y_train, Y_rem = train_test_split(X,Y,train_size=0.7)
X_valid, X_test, Y_valid, Y_test = train_test_split(X_rem,Y_rem,train_size = 2/3)

X_train

X_valid

X_test

"""Part A Q2

"""

import numpy as np

from sklearn import linear_model, svm
from sklearn import datasets

from sklearn.model_selection import train_test_split

np.random.seed(5)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

perceptron_clf = linear_model.Perceptron(max_iter = 500)

perceptron_clf.fit(x_train, y_train)

perceptron_clf.score(x_test, y_test)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

print(x_test)

print(y_test)

"""Part A Q3"""

from random import seed
from random import randrange
from csv import reader
 
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split
 
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 
# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0
 
# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
	return weights
 
# Perceptron Algorithm With Stochastic Gradient Descent
def perceptron(train, test, l_rate, n_epoch):
	predictions = list()
	weights = train_weights(train, l_rate, n_epoch)
	for row in test:
		prediction = predict(row, weights)
		predictions.append(prediction)
	return(predictions)
 
# Test the Perceptron algorithm on the sonar dataset
seed(1)
# load and prepare data
filename = '/content/drive/MyDrive/IML Lab/data_banknote_authentication.txt'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert string class to integers
str_column_to_int(dataset, len(dataset[0])-1)
# evaluate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 500
scores = evaluate_algorithm(dataset, perceptron, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

n_folds = 4
l_rate = 0.01
n_epoch = 500
scores = evaluate_algorithm(dataset, perceptron, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

"""Part B Q1"""

svm_clf = svm.SVC(C=5, kernel='rbf')

svm_clf.fit(x_train, y_train)

y_predict = svm_clf.predict(x_test)

import sklearn
sklearn.metrics.accuracy_score(y_predict,y_test)

svm_clf.score(x_test, y_test)

svm_clf = svm.SVC(C=2, kernel='rbf')

svm_clf.fit(x_train, y_train)

svm_clf.score(x_test, y_test)