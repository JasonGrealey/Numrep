import random
import math
import numpy as np
from mygaussianpdf import MyGaussianPDF
import matplotlib.pyplot as plt

def main():

    mean = 0
    stdev = 1
    a=-5.0
    b=5.0
    gauss = MyGaussianPDF(mean,stdev,a,b)

   # print(gauss.eval(5))
    fmax = gauss.max()
    #getting random value between -5,5 using ran class in previous file
    #print(gauss.ran())

    file = open("pdf.txt", "w")   
    data = []
    #now printing loop
    for i in range (5000):
        #calculating random value
        nexval = gauss.next()
        data.append(nexval)

        #file.write( i , val)
    plt.hist(data, bins=20)
    plt.show()

    print(gauss.integralnumeric(-500,500))
    print(gauss.analyticint(-500,500))

main()

