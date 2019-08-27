import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

print("SVM model using scikit_learn.")

x1=[2.327868056,3.032830419,4.485465382,3.684815246,2.283558563,7.807521179,6.132998136,7.514829366,5.502385039,7.432932365]
x2=[2.458016525,3.170770366,3.696728111,3.846846973,1.853215997,3.290132136,2.140563087,2.107056961,1.404002608,4.236232628]
y=[-1,-1,-1,-1,-1,1,1,1,1,1]

x1 = np.array(x1).reshape(-1, 1)
x2 = np.array(x2).reshape(-1, 1)
x = np.column_stack([x1, x2])
print(x, y)

SVM = SVC()
SVM.fit(x, y)
print("intercept", SVM.intercept_)

y_pred = SVM.predict(x)
print (x,y_pred)
print ("Accuracy is the model of", SVM.score(x, y))
