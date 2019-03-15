#!/usr/bin/env python

import os
import re
import random
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import iplot, init_notebook_mode

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn import neighbors, metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings('ignore')  # "error", "ignore", "always", "default", "module" or "once"

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
X= wine.data
y = wine.target
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2,random_state=0)

def KNN_PredictWine():
    clf = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("\nconfusion_matrix")
    print(metrics.confusion_matrix(y_test, y_pred))
    print("\nclassificatio_report")
    print(metrics.classification_report(y_test, y_pred))
    print("\nf1_score")
    print(metrics.f1_score(y_test, y_pred, average="macro"))
    print("\n")
    print("performance of estimator")
    expected = y_test
    matches = (y_pred == expected)
    print(matches.sum() / float(len(matches)))
    print("\n")

def Gaussian_PredictWine():
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    expected = y_test
    matches = (y_pred == expected)
    print("\nconfusion_matrix")
    print(metrics.confusion_matrix(y_test, y_pred))
    print("\nclassificatio_report")
    print(metrics.classification_report(y_test, y_pred))
    print("\nf1_score")
    print(metrics.f1_score(y_test, y_pred, average="macro"))
    print("\n")
    print("performance of estimator")
    print("\n")
    print(matches.sum() / float(len(matches)))


def DecisionTree():
    from sklearn.tree import DecisionTreeClassifier
    dtree = DecisionTreeClassifier(max_depth=10, random_state=101, max_features=None, min_samples_leaf=15)
    dtree.fit(X_train, y_train)
    y_pred = dtree.predict(X_test)
    print("\nconfusion_matrix")
    print(metrics.confusion_matrix(y_test, y_pred))
    print("\nclassificatio_report")
    print(metrics.classification_report(y_test, y_pred))
    print("\nf1_score")
    print(metrics.f1_score(y_test, y_pred, average="macro"))
    print("\n")
    print("performance of estimator")
    expected = y_test
    matches = (y_pred == expected)
    print(matches.sum() / float(len(matches)))
    print("\n")

def Stochastic():
    from sklearn.linear_model import SGDClassifier
    sgd = SGDClassifier(max_iter=1000,tol=0.19)
    sgd.fit(X_train, y_train)
    y_pred = sgd.predict(X_test)
    print("\nconfusion_matrix")
    print(metrics.confusion_matrix(y_test, y_pred))
    print("\nclassificatio_report")
    print(metrics.classification_report(y_test, y_pred))
    print("\nf1_score")
    print(metrics.f1_score(y_test, y_pred, average="macro"))
    print("\n")
    print("performance of estimator")
    expected = y_test
    matches = (y_pred == expected)
    print(matches.sum() / float(len(matches)))
    print("\n")

def Wine():
    print("\n* * * * * * *   K-NEAREST NEIGHBOUR   * * * * * * * * *\n")
    KNN_PredictWine()
    print("\n* * * * * * *   Gaussian   * * * * * * * * *\n")
    Gaussian_PredictWine()
    print("\n* * * * * * *   Decision Tree   * * * * * * * * *\n")
    DecisionTree()
    print("\n* * * * * * *   Stochastic Gradient Descent   * * * * * * * * *\n")
    Stochastic()
    print("\n* * * * * * * * * * * ** * * *")
    print("*                            * ")
    print("*        THE END             * ")
    print("*                            * ")
    print("* * * * * * * * ** * * * * * *\n\n")



Wine()


