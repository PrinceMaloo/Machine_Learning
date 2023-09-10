# -*- coding: utf-8 -*-
"""B21CH025.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYZg88absmiy5cDz2LgGAuTDRM1xKAI7
"""

# Q_1_(b) Perform data preprocessing steps according to the previous lab (remove Null/NaN
#values, reduce noise, normalize/scale the features etc.).
import pandas as pd
df = pd.read_csv('diabetes(1).csv')
df.isnull().sum()
df = df[df.SkinThickness!=0]
df= df[df.Insulin !=0]
df= df[df.BloodPressure !=0]
X=df.drop('Outcome',axis='columns')
y=df["Outcome"]
X
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit(X)
scaled
X_scaled=scaler.transform(X)

# Q_1_(c) Split the dataset into training-validation-test splits in the ratio of 70:20:10.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled,y, test_size=0.3)

# Q_2_(a) Using sklearn library, perform KNN classification (take n_neighbours=4). You may use
# any distance/similarity function of your choice.
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 4)
classifier.fit(X_train, y_train)
classifier.score(X_test,y_test)

# Q_2_(b) Vary the value of n_neighbours (k) from 4 to 10, and calculate the classification accuracy
# score for each value of k. Discuss in your report the significance of k and how the value
# of k affects the classification accuracy.
for i in range(4,11):
  model = KNeighborsClassifier(n_neighbors = i)
  model.fit(X_train, y_train)
  print(model.score(X_test,y_test))
  
df.describe()

# Q_2_(c) Implement KNN from scratch (without using sklearn library, although the use of NumPy
# and pandas is allowed) using the same distance/similarity function as before. For
# different values of ‘k’, compare its results with those obtained in part (e).
import numpy as np

class KNN:
    def __init__(self,k,X_train,y_train):
        self.x_train=X_train
        self.y_train=y_train
        self.k=k

    def __minkowski_distance(self,x1,x2,p=1):
        return np.power(np.sum(np.power(np.abs(x1-x2),p)),1/p)

    def get_k_nearest_neighbours(self,x_test):
        distances = []
        for i in range(len(self.x_train)):
          try:
            dist=__minkowsko_distance(np.array(self.x_train.columns))
            row=[df.iloc[i,j] for j in range(len(self.x_train.columns))]
            dist=self.__minkowski_distance(np.array(x_test),np.array(row),2)
            distances.append((dist,self.y_train[i]))
          except:
            continue
        distances.sort(key=lambda x: x[0])
        return distances[:self.k]

    def predict(self,x_test):
        distances=self.get_k_nearest_neighbours(x_test)
        yes=0
        no=0
        for i in distances:
            if i[1]==1:
                yes+=1
            else:
                no+=1
        if yes>no:
            return 1
        return 0

#X_train, X_test, y_train, y_test 
model=KNN(4,X_train,y_train)
accuracy=0
sum=0
for i in range(len(X_test)):
  row=[pd.DataFrame(X_test).iloc[i,j] for j in range(len(pd.DataFrame(X_test).columns))]
  result=model.predict(row)
  try:
    if result == y_train[i]:
      sum+=1
  except:
    continue
accuracy=sum/len(X_test)

print("Accuracy",accuracy)

# Q_3_(a) Identify the two real-valued variables/features which have the largest standard deviation
# among all the features. Create a smaller dataset using these two features and the target
# column “outcome” for use in the next parts
X_new_1=df['Insulin']
X_new_2=df['Glucose']
y_new=df['Outcome']
from sklearn.model_selection import train_test_split
X_train_new_1, X_test_new_1, y_train_new, y_test_new = train_test_split(X_new_1, y_new, test_size=0.2)
X_train_new_2, X_test_new_2, y_train_new, y_test_new = train_test_split(X_new_2, y_new, test_size=0.2)

# Q_3_(b),(c) For each of the features obtained in the previous part, you are required to predict the
#target variable using only one variable at a time and using the Bayes Classification
#method. For a given feature, you need to choose an appropriate bin-size to discretize
#the continuous variables into bins (of histogram) such that the classification accuracy is
#maximum.
from sklearn.preprocessing import KBinsDiscretizer
bin_disc = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='uniform')
X_train_transformed = bin_disc.fit_transform(X_train_new)

req_cols=["Insulin","Glucose"]
new_dataset=df[req_cols]

#make a bayes classfier 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



#split data into train and test data
for i in req_cols:

  X_train, X_test, y_train, y_test = train_test_split(new_dataset[i], y_new, test_size=0.2, random_state=42)
  X_train=np.array(X_train).reshape(-1, 1)
  #create bayes classifier
  bayes = GaussianNB()
  #train the model
  bayes.fit(X_train, y_train)

  y_pred = bayes.predict(np.array(X_test).reshape(-1,1))

  print(accuracy_score(y_test, y_pred))