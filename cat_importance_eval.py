# -*- coding: utf-8 -*-
"""cat_importance_eval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1icpEh7QvpI4UPq8Php4cqYbcFookkFKc
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import Normalizer

from google.colab import drive
drive.mount('/content/drive')

data_training=pd.read_csv('/content/drive/MyDrive/PhD/Polyvore_Outfit/disjoint/cat_id_training_set.csv')
data_test=pd.read_csv('/content/drive/MyDrive/PhD/Polyvore_Outfit/disjoint/cat_id_test_set.csv')

data_training = data_training.sample(frac=1).reset_index(drop=True)
data_test = data_test.sample(frac=1).reset_index(drop=True)

'''X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, 1:5].values, data['Target'].values
                                                    , test_size=0.3, random_state=5)'''

clf = DecisionTreeClassifier(max_depth=6,)
clf = clf.fit(data_training.iloc[:, 1:],data_training['Target'])

y_pred = clf.predict(data_test.iloc[:, 1:])

print("Accuracy:",metrics.accuracy_score(data_test['Target'], y_pred))

print(confusion_matrix(data_test['Target'],y_pred))
print(classification_report(data_test['Target'],y_pred))

from sklearn.neural_network import MLPClassifier

transformer = Normalizer()
x_test=transformer.transform(data_test.iloc[:, 1:])
x_train=transformer.transform(data_training.iloc[:, 1:])

mlp = MLPClassifier(hidden_layer_sizes=(4), activation='relu', solver='adam', max_iter=50)

mlp.fit(x_train,data_training['Target'])

predict_train = mlp.predict(x_train)
predict_test = mlp.predict(x_test)

print(confusion_matrix(data_training['Target'],predict_train))
print(classification_report(data_training['Target'],predict_train))

print(confusion_matrix(data_test['Target'],predict_test))
print(classification_report(data_test['Target'],predict_test))

predict_test[1:100]

from sklearn.linear_model import LogisticRegression

lrg = LogisticRegression(random_state=0).fit(data_training.iloc[:, 1:],data_training['Target'])

predict_train = lrg.predict(data_training.iloc[:, 1:])
predict_test = lrg.predict(data_test.iloc[:, 1:])

print(confusion_matrix(data_training['Target'],predict_train))
print(classification_report(data_training['Target'],predict_train))

print(confusion_matrix(data_test['Target'],predict_test))
print(classification_report(data_test['Target'],predict_test))
