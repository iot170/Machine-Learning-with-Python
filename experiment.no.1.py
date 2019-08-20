import numpy as np
import matplotlib.pyplot as plt

print("Code By Umesh Tyagi")
# Create two array for the x abd y
x = np.array([1, 2, 4, 3, 5])
y = np.array([1, 3, 3, 2, 5])
print('Value of X:', x)
print('Value of y:', y)


# print plot for x and y
#plt.scatter(x, y)
#plt.ylabel("Dependent variable Y")
#plt.xlabel("Independent variable X")
#plt.show()

# Calculate the mean
mean_x = np.mean(x)
mean_y = np.mean(y)

# Calculate the slope
upper = np.sum((x - mean_x) * (y - mean_y))
lower = np.sum((x - mean_x) * (x - mean_x))
b1 = upper / lower
print('Value of Slope:', b1)

# Calculate the intercept
b0 = mean_y - b1 * mean_x
print('Value of Intercept:%.3f' %b0)

y_pred = []
for i in range(len(x)):
    y_p = b0 + b1 * x[i]
    y_pred.append(y_p)
print("Y Predict", y_pred)

# Calculate predict value
#y1 = b0 + b1 * x[0]
#y2 = b0 + b1 * x[1]
#y3 = b0 + b1 * x[2]
#y4 = b0 + b1 * x[3]
#y5 = b0 + b1 * x[4]

#y_pred = np.array([y1, y2, y3, y4, y5])
#print('Predict Value:', y_pred)



# square and mean
error = np.mean((y_pred - y) * (y_pred - y))
print("Mean Square Error", error)

# sqrt
rmse = np.sqrt(error)
print("Root Mean Square Error", rmse)

# plot actual value and predict value
plt.scatter(x, y)
plt.scatter(x, y_pred)
plt.show()