import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

data = pd.read_csv('data/bestsellers with categories.csv')

print(data.head(5))

print(data.shape)

data.info()

X=data[['Reviews', 'Price', 'Year', 'Genre']]
X=pd.get_dummies(X, drop_first=True)
y=(data['User Rating'] > 4.5).astype(int)

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=0)
print(len(X_train))
print(len(X_test))

model=RandomForestClassifier(n_estimators=100, max_depth=None, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y.value_counts())

print('Raport')
print(classification_report(y_test, y_pred))

print('Dokładność')
print(accuracy_score(y_test, y_pred))

joblib.dump(model, 'models/model_v1.joblib')

joblib.dump(X.columns, 'models/model_columns.joblib')
print('Model i kolumny zapisane')


