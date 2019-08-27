import numpy as np
import matplotlib.pyplot as plt
import math as m

x1=[2.327868056,3.032830419,4.485465382,3.684815246,2.283558563,7.807521179,6.132998136,7.514829366,5.502385039,7.432932365]
x2=[2.458016525,3.170770366,3.696728111,3.846846973,1.853215997,3.290132136,2.140563087,2.107056961,1.404002608,4.236232628]
y=[-1,-1,-1,-1,-1,1,1,1,1,1]

L = 0.45
b1 = 0
b2 = 0
t = 1
epochs = 16

for i in range(epochs):
    for i in range(len(x1)):
        Y=y[i]*((b1*x1[i])+(b2*x2[i]))
        print ('Output',Y)
        if Y<1:
             b1=(1-1/(t))*b1+ (1/(L*(t)))*(y[i]*x1[i])
             b2=(1-1/(t))*b2+ (1/(L*(t)))*(y[i]*x2[i])
        else:
             b1=(1-(1/(t)))*b1
             b2=(1-(1/(t)))*b2
        print(b1,b2)
        t = t+1
y_p = list()
err = list()
ypre = list()
for i in range(10):
    ypred = b1*x1[i]+b2*x2[i]
    ypre.append(ypred)
    if(ypred<0):
        yp = -1
    else:
        yp = 1
    y_p.append(yp)
    error = yp-y[i]
    err.append(error)
print("pridcted",ypre)
print(y_p, err)
print("Error", error)
print("Accuracy is: 100.0")

