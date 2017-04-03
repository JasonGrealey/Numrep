# first we shall import the data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def main():
    filename = "DecayTimesData.txt"
    fi = np.loadtxt(filename)
    print("first t value is " '{}' .format(fi[0]))
    #hist = np.histogram(f,bins=20)
    #plt.hist(fi,bins=100)
    #plt.show()


    #function for PDF
    def pdf(t,tau1,tau2,f):
        # print("KEK >>>>>> ",tau1,tau2,f)
        val = f*(1/tau1)*np.exp(-(t/tau1)) + (1-f)*(1/tau2)*np.exp(-(t/tau2))
        print (val)
        return val
    
    
    def pdfnll(t,params):
        f = params[2]
        tau1 = params[0]
        tau2 = params[1]
        nll = -1*(np.log(pdf(t,tau1,tau2,f)+0.00000001))#epsilon so we never have zero
        return nll
        
    testval = pdfnll(fi[0],[0.5,0.5,0.5])
    print ("NLL contribution from val i is " '{}' .format(testval))
    
    yvals = [pdfnll(fi[i],[0.5,0.5,0.5]) for i in range(len(fi))]
    nlltest = np.sum(yvals)
    
    def nll(params,vals):
        #f = params[2]
        #tau1 = params[0]
        #tau2 = params[1]
        return np.sum(pdfnll(vals, params))
    

    bnds = np.array([[0]*3, [float("inf")]*2 + [1] ]).T
    nlltest2= nll(fi,[0.5,0.5,0.5])
    print ("NLL from whole method is  " '{}' .format(nlltest2))
    initparams = np.asarray([0.5,1,1])
    #NLL = lambda vals,*args: nll(vals,*args)
    Nll = lambda:nll(data, args), 
    #x0=[0,0]
    print(nll, type(nll))
    result = minimize(nll,x0=initparams, args=(fi,), bounds=bnds, method='SLSQP')
    print(result)
    '''
    initparams = [0.5,0.5,0.5]
    #nllopt = minimize(nll,x0 = initparams,args=(fi,))
    nllopt = minimize(nll(fi,initparams),x0 =initparams)
    print(nllopt.x)
    print("NLL initially is " '{}' .format(nlltest))
    #plt.hist(test,bins=20)
    '''
    #plt.show()
main()
