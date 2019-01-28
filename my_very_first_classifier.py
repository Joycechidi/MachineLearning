# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:50:59 2019

@author: JChidiadi
"""

#How to buld my own classifier from scratch
#K in KNearest neighbor means Number of neighbors to consider
#You find the most nearest neighbor then get the Euclidean Distance

#d(a,b) = sqrt((x2 - x1)**2 + (y2 - y1)**2)
#A Scrappy version of KNearest Neighbors


from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)


class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(self.y_train)
            predictions.append(label)
        return predictions
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


            

from sklearn import datasets
iris = datasets.load_iris()


X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

#We can use KNeearest Neighbours instead of the DecisionTree
#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))

