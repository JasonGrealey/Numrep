#class for making y=mx+c

import numpy as np
# Read in the data
print("Reading in coefficients matrix")
coeffs = np.loadtxt("testData.txt")
print(coeffs)

def predy(m,x,c):
    y = m*x + c
ypred = np.zeros(10)

m0 = 0
c0 = 1
for x in range ((10)+1):
    ypred[x]=0




for x in range (10):
    ypred[x] = predy(m0,x,c0)
    print(str(ypred[x]))
