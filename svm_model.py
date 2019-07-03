import pandas as pd
from preprocessing import preprocess


data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\train_tweets.xlsx')
data = data[['content','positivity']]
data['content'] = data['content'].apply(lambda x: preprocess(x))
data = data[data['positivity'] !='notr']
data = data[pd.notnull(data['positivity'])]

td = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\test_tweets.xlsx')
td = td[['content','positivity']]
td['content'] = td['content'].apply(lambda x: preprocess(x))
td = td[pd.notnull(td['positivity'])]
td = td[td['positivity'] !=2]
td = td[pd.notnull(td['positivity'])]

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=5,ngram_range=(1, 3))
train_vectors = vectorizer.fit_transform(data['content'])
test_vectors = vectorizer.transform(td['content'])

import time
from sklearn import svm
from sklearn.metrics import classification_report

classifier_linear = svm.SVC(kernel='linear')
t0 = time.time()
classifier_linear.fit(train_vectors, data['positivity'])
t1 = time.time()
prediction_linear = classifier_linear.predict(test_vectors)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1

print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
report = classification_report(td['positivity'], prediction_linear, output_dict=True)
print('positive: ', report['olumlu'])
print('negative: ', report['olumsuz'])