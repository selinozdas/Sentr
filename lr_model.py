import pandas as pd
import numpy as np
import re, os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
from preprocessing import preprocess
from param import data,vect,X_train, X_test, y_train, y_test
'''Create, train and validate model'''
X_train_vectorized = vect.transform(X_train)
model = LogisticRegression(solver='liblinear')
model.fit(X_train_vectorized, y_train)
filename = 'lr_model.sav'
joblib.dump(model, filename)
