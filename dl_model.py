import joblib
filename = 'model.h5'
model = joblib.load(open(filename, 'rb'))