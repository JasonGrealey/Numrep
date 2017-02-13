import random
import math
import numpy as np

class MytauPDF():
    #initalisation with mean and stdev given
    def __init__(self,tau,a,b):
        self.tau = tau
        self.a=a
        self.b=b
    #method takes upper, lower, xval and stretches it to scale
    def ran(self):
        xval  =  random.random()
        scaledrand=self.a + (self.b-self.a)*xval
        return scaledrand

    #method for getting result of gaussian given xvalue
    def eval(self, xval):
        result = (1.0/(self.tau))*(np.exp(-1.0*(xval/self.tau)))
        return result

        #evaluating gaussian at mean is maximum
    def max(self):
        val = self.eval(0.0)
        return val

    def next(self):
        y2=1.0
        y1=0.0
        xscal = 0.0
        while y2>y1:
            xscal = self.ran()
            y1 = self.eval(xscal)
            y2 = random.random()
            y2 = self.max()*y2
            if y2<=y1:
                return xscal
            else:
                continue 

    def integralnumeric(self,low,high):
        #numsteps
        n = 1000000
        ninside=0
        #here we have rectangle from low to high and sligltly above function 
        base = abs(high-low)
        height = self.max()
        #area of total sampling area triangle
        
        for i in range(n):
            #random xvalue between integration boudaries
            xvalue = low + random.random()*base
            #choosing random y from 0->max function 
            yrand = random.random()*height
            yfunc = self.eval(xvalue)
            if yfunc >= yrand:
                ninside = ninside + 1
        

        #area of square
        totarea = (base*height)
        #fraction to inside over total
        frac = ninside/n
        
        area = totarea*frac
        return area

    def analyticint(self,low,high):
        answer = -1.0*np.exp(-1.0*(high/(self.tau))) + 1.0*np.exp(-1.0*(low/(self.tau))) 
        return answer


