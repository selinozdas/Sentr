from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from preprocessing import preprocess
import pandas as pd 
import numpy as np
from keras.preprocessing.text import Tokenizer
from sklearn.metrics import classification_report

model = load_model('model.h5')
td = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\test_tweets2.xlsx')
td = td[['content','positivity']]
td['content'] = td['content'].apply(lambda x: preprocess(x))
td = td[pd.notnull(td['positivity'])]
td = td[td['positivity'] !=2]
#print(td.content.str.split(expand=True).stack().value_counts())
data = pd.read_excel(r'C:\Users\slnoz\Desktop\Sentiment\train_tweets2.xlsx')
data = data[['content','positivity']]
data['content'] = data['content'].apply(lambda x: preprocess(x))
data = data[data['positivity'] != 2]
data = data[pd.notnull(data['positivity'])]
#print(data.content.str.split(expand=True).stack().value_counts())
max_fatures = 30000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['content'].values)
X1 = tokenizer.texts_to_sequences(td['content'].values)
X1 = pad_sequences(X1,maxlen=742)
Y1 = pd.get_dummies(td['positivity']).values
pred = model.predict(X1,batch_size=32, verbose=2)
y_pred_bool = np.argmax(pred, axis=1)

pos_cnt, neg_cnt, pos_correct, neg_correct, overall_correct, overall_cnt = 0, 0, 0, 0, 0, 0
for x in range(len(X1)):
    result = model.predict(X1[x].reshape(1,X1.shape[1]),batch_size=1,verbose = 2)[0]
    overall_cnt +=1
    if np.argmax(result) == np.argmax(Y1[x]):
        overall_correct +=1
        if np.argmax(Y1[x]) == 0:
            neg_correct += 1
        else:
            pos_correct += 1      
    if np.argmax(Y1[x]) == 0:
        neg_cnt += 1
    else:
        pos_cnt += 1

print("pos_acc", pos_correct/pos_cnt*100, "%")
print("neg_acc", neg_correct/neg_cnt*100, "%")
print('overall_acc', overall_correct/overall_cnt*100,'%')
