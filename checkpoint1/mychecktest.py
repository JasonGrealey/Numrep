import random
import math
import numpy as np
from mytaupdf import MytauPDF
import matplotlib.pyplot as plt

def main():
    #defining vars
    tau=2.2e-3
    a=0.0
    b=10*tau
    #initialising tau distribution
    expon = MytauPDF(tau,a,b)
   # print(expon.eval(0))
   # print(1/tau)
    fmax = expon.max()
    #getting random value between 0, 5 lifetimes using ran class in previous file
    #print(gauss.ran())

    #file = open("pdf.txt", "w")   
    data = []
    #now loop for printing  
    for i in range (1000):
        #calculating random value
        nexval = expon.next()
        data.append(nexval)
        
        #file.write( i , val)
    #plt.hist(data, bins=20)
    #plt.show()
    tauobs = np.average(data)
    print("'observed tau' from one experiment is shown below:")
    print(tauobs)



    #here we are going to perform the 'experiment' 500 times and get a calulation for tau
    #defining lists
    newdata=[]
    taulist = []
    tauten = []
    stlist = []
    #now we want to do the previous 'experiment' 500 times
    for i in range (500):
        for j in range (1000):
            nextval = expon.next()
            newdata.append(nextval)
        #here calculate tau to get a look at stderr over time
        if i == 10:
            #tau is mean
            tautennew = np.mean(newdata)
            #empyting the experiment list
            newdata=[]
            stdevten = np.std(taulist)
            stderrten = stdevten/math.sqrt(10)
        else :
            taunew = np.mean(newdata)
            newdata=[]
            taulist.append(taunew)
    
    tautot = np.mean(taulist)
    stdev = np.std(taulist)
    #standard error
    stderr = stdev/math.sqrt(500)
    print(" the value of tau after 500 experiments is %s" % (tautot))
    print("this is the standard deviation of tau over the 500 vs 10 experiments %s , %s" % (stdev,stdevten))
    print("standard error for 500 vs 10 experiments  %s , %s  " % (stderr, stderrten))
    #plt.hist(taulist,bins=9)
    #plt.show()

    #making a combined plot
    plt.figure(1)
    plt.subplot(211)
    plt.hist(data,bins=20)
    plt.title('Showing decay of distribution')
    plt.subplot(212)
    plt.hist(taulist,bins=9)
    plt.title('Binned values of tau')
    plt.show()
    
    print("here are are doing numerical integration")
    print(expon.integralnumeric(0,0.002))
    print(" here we are doing analytic integration")
    print(expon.analyticint(0,0.002))
    
main()

