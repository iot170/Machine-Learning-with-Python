import numpy as np

# input data
ix1 = np.array([3.393533, 3.110073, 1.343809, 3.582294, 2.280362, 7.423437, 5.745052, 9.172169, 7.792783, 7.939821])
ix2 = np.array([2.3313, 1.7815, 3.3684, 4.6792, 2.867, 4.6985, 3.534, 2.5111, 3.4241, 0.7916])
iy = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# codebook vector
cx1 = np.array([3.58229404, 7.79278348, 7.93982082, 3.39353321])
cx2 = np.array([0.7916372, 2.3312734, 2.8669903, 4.6791791])
cy = np.array([0, 0, 1, 1])


alpha = 0.7
pred = []

for i in range(len(ix1)):
    ddistance = []
    for j in range(len(cx1)):
        A = np.sum((ix1[i] - cx1[j]) ** 2 + (ix2[i] - cx2[j]) ** 2)
        Distance = np.sqrt(A)
        ddistance.append(Distance)
    print(ddistance)
    bmu = np.min(ddistance)
    print(bmu)

    for n in range(len(cx1)):
        if ddistance[n]==bmu:
            m=n
            print("index is ",m)

    if iy[i]==cy[m]:
        new1=cx1[m]+alpha * (ix1[i]-cx1[m])
        new2=cx2[m]+alpha * (ix2[i]-cx2[m])

    else:
        new1=cx1[m]-alpha * (ix1[i]-cx1[m])
        new2=cx2[m]-alpha * (ix2[i]-cx2[m])

    cx1[m]=new1
    cx2[m]=new2
    print("update x1 is ",cx1)
    print("update x2 is ",cx2)


print("######################################################################")
for i in range(len(ix1)):
    dddistance = []
    for j in range(len(cx1)):
        Aa = np.sum((ix1[i] - cx1[j]) ** 2 + (ix2[i] - cx2[j]) ** 2)
        dDistance = np.sqrt(Aa)
        dddistance.append(dDistance)
    print("New Distance", dddistance)
    bmuu = np.min(dddistance)
    print("New BMU", bmuu)


    for n in range(len(cx1)):

        if dddistance[n] == bmuu:
            m=n
            mm = cy[m]
            pred.append(mm)
            print("index is ",m)
print("##################################")
print("Pred", pred)
print("Actual Value is",iy)

error = iy - pred
print("error",error)

accuracy = ((len(iy)) - sum(error))/(len(pred))*100
print(accuracy, "%")


