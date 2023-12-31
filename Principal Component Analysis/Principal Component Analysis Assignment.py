# -*- coding: utf-8 -*-
"""Lab7_B21CH025

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-xh45JHDH6Az-CsLgBDbp7XiEvcDkst
"""

from google.colab import drive
drive.mount('/content/drive')

"""Q1.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn import decomposition
from sklearn import datasets

from sklearn.model_selection import train_test_split

np.random.seed(5)

iris_data =pd.read_csv('/content/drive/MyDrive/IML Lab/iris.datas - iris.datas.csv', encoding='windows-1252')

iris_data

iris_data.describe()

iris_data.info()

iris_data.isnull()

iris_name =pd.read_csv('/content/drive/MyDrive/IML Lab/iris.names.csv', encoding='windows-1252' , on_bad_lines='skip')

iris_name

iris_name.describe

iris_name.info

iris_name.isnull()



x = iris_data.iloc[:, [0, 1, 2, 3]].values
true_labels = iris_data.iloc[:,-1]
true_labels = true_labels.values
true_labels_list = []
class_names = ['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in true_labels:
  if i=='Iris-setosa':
    true_labels_list.append(1)
  elif i=='Iris-versicolor':
    true_labels_list.append(0)
  else:
    true_labels_list.append(2)

iris_data['species']= true_labels_list
iris_data

"""Q2"""

#Q2 Using knn

X = iris_data
y = iris_data.species1
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=7)

# Training Knn
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)

# Makinng Prediction
y_pred = knn.predict(X_test)

# Calculating Accuracy Score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy -->", accuracy*100)

"""Q3"""

iris = datasets.load_iris(as_frame=True)

X = iris.data
y = iris.target

X.head()

sns.distplot(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

pca = decomposition.PCA(n_components=3)
pca.fit(x_train)

transformed_X = pca.transform(x_train)

# first 2 transformed samples
transformed_X[:2]

pca.components_.shape

# How much variance do these components capture?

pca.explained_variance_ratio_

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(transformed_X, y_train)

# evaluate
from sklearn.metrics import accuracy_score


x_test_transformed = pca.transform(x_test)
y_pred = clf.predict(x_test_transformed)

acc = accuracy_score(y_pred, y_test)

print(acc)

"""Q4"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.decomposition import PCA



pca = PCA(n_components=3)
train_projected = pca.fit_transform(X_train)
test_projected = pca.fit_transform(X_test)

k_range = range(1,121)
scores = {};
scores_list = [];
for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_projected,y_train)
    pred = knn.predict(test_projected)
    scores[i] = metrics.accuracy_score(y_test,pred)
    scores_list.append(metrics.accuracy_score(y_test,pred))

print('Scores ', scores,'\n')
print('Scores List ',scores_list,'\n')

"""Q5"""

pca = decomposition.PCA(n_components=2)
pca.fit(x_train)

transformed_X = pca.transform(x_train)

# first 2 transformed samples
transformed_X[:2]

pca.components_.shape

# How much variance do these components capture?

pca.explained_variance_ratio_

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(transformed_X, y_train)

# evaluate
from sklearn.metrics import accuracy_score


x_test_transformed = pca.transform(x_test)
y_pred = clf.predict(x_test_transformed)

acc = accuracy_score(y_pred, y_test)

print(acc)

pca = decomposition.PCA(n_components=4)
pca.fit(x_train)

transformed_X = pca.transform(x_train)

# first 2 transformed samples
transformed_X[:2]

pca.components_.shape

pca.explained_variance_ratio_

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(transformed_X, y_train)

# evaluate
from sklearn.metrics import accuracy_score


x_test_transformed = pca.transform(x_test)
y_pred = clf.predict(x_test_transformed)

acc = accuracy_score(y_pred, y_test)

print(acc)