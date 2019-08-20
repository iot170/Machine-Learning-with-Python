#Logicstic regression

import numpy as np
import matplotlib.pyplot as plt

x = np.array([123,124,149,100,156,178,120,110,167,174,111,109])
y = np.array([0,0,1,0,1,1,0,0,1,0,1,0])

xmean = np.mean(x)
print('Mean of height', xmean)

ymean = np.mean(y)
print('Mean of label', ymean)

upper = np.sum((x - xmean) * (y - ymean))
lower = np.sum((x - xmean) * (x - xmean))

b1 = upper / lower
print('Slope', b1)

b0 = ymean - b1*xmean
print('Intercept', b0)

z = []
ydes = []
for i in range(len(x)):
    znew = b0 + b1 * x[i]
    z.append(znew)
    sig1 = np.exp(znew)
    sigmoid1 = sig1/(1+sig1)
    ydes.append(sigmoid1)

print('Value of Z', z)
print('Value of Sigmoid', ydes)


for i in range(len(ydes)):
    if(ydes[i]<=0.5):
        print('class 0 = Female')
    else:
        print('class 1 = Male')



plt.scatter(x, z)
plt.show()





