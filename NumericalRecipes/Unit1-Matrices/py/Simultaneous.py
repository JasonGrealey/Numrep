import numpy as np


#......................................................................
#Class to provide a method to calculate chisq
def main():
    
    print("Solving simultaneous equations")


    # Read in the data
    print("Reading in coefficients matrix")
    coeffs = np.loadtxt("SimultaneousMatrix.txt")

    print("Reading in vector")
    vector = np.loadtxt("SimultaneousVector.txt")
    
    # Create matrices
    mcoeffs = np.matrix(coeffs)
    mvector = np.matrix(vector).T

    print(str(mcoeffs))
    print(str(mvector))


    result = mcoeffs.I * mvector

    print("\n Result is")
    print(str(result))


main()


