from param import vect
import joblib
model = joblib.load('lr_model.sav')

def predict_df(new_data):
    predictions = model.predict(vect.transform(new_data))
    return predictions

def predict_str(new_string):
    new_data = [new_string]
    predictions = model.predict(vect.transform(new_data))
    return predictions
