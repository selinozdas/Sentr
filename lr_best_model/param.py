from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import os
import joblib
import pandas as pd
from preprocessing import preprocess
abs_path = os.path.dirname(os.path.abspath(__file__))
file_name = "train_tweets.xlsx"
path = os.path.join(abs_path,file_name)
data = pd.read_excel(path)
data = data[['content','positivity']]
data['content'] = data['content'].apply(lambda x: preprocess(x))
data = data[data['positivity'] !='notr']
data = data[pd.notnull(data['positivity'])]

X_train, X_test, y_train, y_test = train_test_split(data['content'], data['positivity'], random_state = 1,train_size = 0.99)
vect = CountVectorizer(min_df = 3, ngram_range = (1,3)).fit(X_train)
X_train_vectorized = vect.transform(X_train)

