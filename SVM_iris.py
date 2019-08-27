import numpy as np
import pandas as pd
from sklearn.svm import SVC

print("clf model using scikit_learn and iris")

df = pd.read_csv('E:\iris.csv')
x = np.array(df['sepal.length'], df['sepal.width']).reshape(-1, 1)
y = np.array(df['variety'])
#print(x, y)

clf = SVC()
clf.fit(x, y)
#print("intercept", clf.intercept_)
y_pred = clf.predict(x)
print (x,y_pred)
print ("Accuracy is the model of", clf.score(x, y))
