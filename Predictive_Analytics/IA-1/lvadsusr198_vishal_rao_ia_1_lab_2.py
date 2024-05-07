# -*- coding: utf-8 -*-
"""LVADSUSR198 Vishal Rao IA-1 Lab- 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AMangsZHL1AMuOcCXUoulPw43Pg4Cg83
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score,confusion_matrix
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

booking_data = pd.read_csv('/content/booking.csv')

booking_data.isna().sum()

booking_data['room type']= booking_data['room type'].fillna(booking_data['room type'])
booking_data['average price']= booking_data['average price'].fillna(booking_data['average price'])

## outlier detetion and removal
avg_price_outliers = sns.boxplot(booking_data['average price'])

booking_data = booking_data[booking_data['average price']<200]

lead_time_outliers = sns.boxplot(booking_data['lead time'])

booking_data = booking_data[booking_data['lead time']<300]

##Encoding the categorical data
lbl_enc = LabelEncoder()
booking_data['type of meal'] = lbl_enc.fit_transform(booking_data['type of meal'])
booking_data['room type'] = lbl_enc.fit_transform(booking_data['room type'])
booking_data['market segment type'] = lbl_enc.fit_transform(booking_data['market segment type'])
booking_data['booking status'] = lbl_enc.fit_transform(booking_data['booking status'])

## dropping features ( feature selection )
#booking_data = booking_data.drop(columns=['date of reservation','Booking_ID'],axis=1)
booking_data

booking_data.corr()

X = booking_data.drop('booking status',axis=1)
y = booking_data['booking status']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


## Scaling the data
scale = MinMaxScaler()
scale.fit(X_train)
x_scaled = scale.fit_transform(X_train)

x_test_s= scale.fit_transform(X_test)

model = LogisticRegression(random_state=0,max_iter=10000)

trained_model = model.fit(x_scaled,y_train)

y_pred = trained_model.predict(x_test_s)

# cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
# print(cnf_matrix)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)

print('Accuracy score: ',round(accuracy*100,2),'%')
print('Precision score: ',round(precision*100,2),'%')
print('Recall score: ',round(recall*100,2))