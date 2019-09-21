import numpy as np
from statistics import mode

x1 = np.array([3.393533, 3.110073, 1.343809, 3.582294, 2.280362, 7.423437, 5.745052, 9.172169, 7.792783, 7.939821])
x2 = np.array([2.3313, 1.7815, 3.3684, 4.6792, 2.867, 4.6985, 3.534, 2.5111, 3.4231, 0.7916])
y = np.array([0,0,0,0,0,1,1,1,1,1])
k = 5

print(x1,x2,y)

nx1 = 8.093607
nx2 = 3.3365732
ddistance = []

for i in range(10):
    A = np.sum((x1[i]-nx1) ** 2 + (x2[i]-nx2) ** 2)
    Distance = np.sqrt(A)
    ddistance.append(Distance)


for i in range(len(ddistance)):
    for j in range(len(ddistance)-i-1):
        if ddistance[j]<ddistance[j+1]:
            ddistance[j],ddistance[j+1]=ddistance[j+1],ddistance[j]
            y[j],y[j+1]=y[j+1],y[j]
print("Distance",ddistance)
print("Y",y)


nbr=list()
for i in range(k):
    nbr.append(y[i])
print(nbr)
knn = mode(nbr)
print(knn)

