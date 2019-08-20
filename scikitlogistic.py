import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print("Logistic model using scikit learn")
df = pd.read_csv('E:\Book1.csv')

x1 = np.array(df['Height']).reshape(-1, 1)
x2 = np.array(df['Weight']).reshape(-1, 1)
x = df[['Height', 'Weight']]
y = df['Gender']

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

regressor = LogisticRegression()
regressor.fit(X_train, y_train)
print("intercept", regressor.intercept_)

y_pred = regressor.predict(X_test)
print (X_test,y_pred)

print ("Accuracy is the model of", regressor.score(X_test,y_test))
plt.figure()
plt.scatter(X_test[y_test == 1].Weight, X_test[y_test == 1].Height, color = 'blue', label = 'Male')
plt.scatter(X_test[y_test == 0].Weight, X_test[y_test == 0].Height, color = 'red', label = 'Female')
plt.show()