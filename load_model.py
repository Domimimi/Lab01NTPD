import pandas as pd
import joblib

model = joblib.load('models/model_v1.joblib')
model_columns = joblib.load('models/model_columns.joblib')

new_book = pd.DataFrame([{
    'Reviews':10000,
    'Price':10,
    'Year':2019,
    'Genre':'Fiction'
}])

new_book = pd.get_dummies(new_book)

new_book = new_book.reindex(columns=model_columns, fill_value=0)

result = model.predict(new_book)

if result[0]==1:
    print('Hit')
else:
    print('No hit')

print(result)
