# -*- coding: utf-8 -*-
"""LVADSUSR198 _Vishal Rao_FA_lab-4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JiPKUD8wTPrfs4Jd9qu3AsMI_ybldQDw
"""

from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df= pd.read_csv('/content/anomaly_train.csv')
df

df.isna().sum()
sns.boxplot(df['Amount'])

df_dropped = df.drop('TransactionID',axis= 1)
df_dum = pd.get_dummies(df_dropped)
df_dum

model = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.1)
model.fit(df_dum)

df['anomaly_score'] = model.decision_function(df_dum)
df.head()
df['result'] = model.predict(df_dum)
df.head()

plt.scatter(data = df, x = 'Amount',y = 'anomaly_score',c = 'result')