import numpy as np
# Read in the data
print("Reading in coefficients matrix")
coeffs = np.loadtxt("SimultaneousMatrix.txt")

print("Reading in vector")
vector = np.loadtxt("SimultaneousVector.txt")
# Create matrices
mcoeffs = np.matrix(coeffs)
mvector = np.matrix(vector).T

print(mcoeffs)
print(mvector)

minverse = np.linalg.inv(mcoeffs)

print(minverse)

manswer = np.matmul(minverse,mvector)
print(manswer)
