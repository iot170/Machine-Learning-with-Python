
import numpy as np
import matplotlib.pyplot as plt

print("Code By Umesh Tyagi")
x=np.array([1.0,2.0,4.0,3.0,5.0])
y=np.array([1.0,3.0,3.0,2.0,5.0])
print("Value of X: ", x)
print("Value of Y: ", y)
b0 = 0
b1= 0

L = 0.01
epochs = 25

for i in range(epochs):
    for i in range(0,4):
        Y_pred = b1*x[i]+b0
        error=Y_pred-y[i]
        b0=b0-(L*error)
        b1=b1-(L*error*x[i])
    print(b0,b1)
print(b0,b1)


rmse = 0
y_pre=[]
for i in range(len(x)):
    y_pred = b0 + b1 * x[i]
    rmse += (y[i] - y_pred) ** 2
    y_pre.append(y_pred)
rmse = np.sqrt(rmse/len(x))
print ("Rmse:", rmse)
print("y_pre is:",y_pre)

plt.scatter(x, y)
plt.plot(x, y_pre, color='red')
plt.show()