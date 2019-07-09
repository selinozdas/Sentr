import pandas as pd
import numpy as np
import matplotlib as plt
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib
from preprocessing import preprocess

'''Create, train and validate model'''
data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\train_tweets.xlsx')
data = data[['content','positivity']]
data['content'] = data['content'].apply(lambda x: preprocess(x))
data = data[data['positivity'] !='notr']
data = data[pd.notnull(data['positivity'])]


X_train, X_test, y_train, y_test = train_test_split(data['content'], data['positivity'], random_state = 1,train_size = 0.8)
vect = CountVectorizer(min_df = 3, ngram_range = (1,3)).fit(X_train)
X_train_vectorized = vect.transform(X_train)
model = RandomForestClassifier()
model.fit(X_train_vectorized, y_train)
filename = 'lr_model.sav'
joblib.dump(model, filename)

predictions = model.predict(vect.transform(X_test))
feature_names = np.array(vect.get_feature_names())
#sorted_coef_index = model.coef_[0].argsort()
sk_report = classification_report(
    digits=6,
    y_true=y_test.to_list(), 
    y_pred=predictions)
print('Evaluation over validation data')
print(sk_report)
sk_report2 = confusion_matrix(
    y_true=y_test.to_list(), 
    y_pred=predictions, labels = ['olumsuz','olumlu'])
print(sk_report2)

'''Predict on test data'''
test_data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\test_tweets.xlsx')
test_data = test_data[['content','positivity']]
test_data['content'] = test_data['content'].apply(lambda x: preprocess(x))
test_data = test_data[pd.notnull(test_data['positivity'])]
test_data = test_data[test_data['positivity'] !='notr']
predictions = model.predict(vect.transform(test_data['content']))


sk_report = classification_report(
    digits=6,
    y_true=test_data['positivity'].to_list(), 
    y_pred=predictions)
print('Evaluation over test data')
print(sk_report)
sk_report2 = confusion_matrix(
    y_true=test_data['positivity'].to_list(), 
    y_pred=predictions, labels = ['olumsuz','olumlu'])
print(sk_report2)


'''Predict on 250 entries of decathlon'''
test_data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\decathlon.xlsx')
test_data = test_data[['content','positivity']]
test_data['content'] = test_data['content'].apply(lambda x: preprocess(x))
test_data = test_data[pd.notnull(test_data['positivity'])]
test_data = test_data[test_data['positivity'] !='notr']
predictions = model.predict(vect.transform(test_data['content']))


sk_report = classification_report(
    digits=6,
    y_true=test_data['positivity'].to_list(), 
    y_pred=predictions)
print('Evaluation over sub-decathlon data')
print(sk_report)
sk_report2 = confusion_matrix(
    y_true=test_data['positivity'].to_list(), 
    y_pred=predictions, labels = ['olumsuz','olumlu'])
print(sk_report2)

def sentiment(entry):
    processed= preprocess(entry)
    result = model.predict(vect.transform([processed]))
    return result[0]

pred_data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\dectest.xlsx')
pred_data = pred_data[['Comment']]
#pred_data = pred_data[pred_data['positivity'] !='notr']
content = pred_data['Comment'].apply(lambda x: preprocess(x))
predictions = model.predict(vect.transform(content))
df = pd.DataFrame({'content':pred_data['Comment'],'processed':content,'predicted':predictions})
df.to_excel(r"C:\Users\slnoz\Desktop\Sentiment\decoutnoneu.xlsx")