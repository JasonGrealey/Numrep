# first we shall import the data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random

def main():
    filename = "DecayTimesData.txt"
    fi = np.loadtxt(filename)
    #print("first t value is " '{}' .format(fi[0]))
    #hist = np.histogram(f,bins=20)
    #plt.hist(fi,bins=100)
    #plt.show()
    meanobst = np.mean(fi)
    cutoff = 9.578530184172956e-08
    #def normfactor(cut):
    #    val =1/(1- np.exp(-cut/
    #function for PDF
    def pdf(t,tau1,tau2,f):
        # print("KEK >>>>>> ",tau1,tau2,f)
        val = f*(1/tau1)*np.exp(-(t/tau1)) + (1-f)*(1/tau2)*np.exp(-(t/tau2))
        return val
    
    
    def pdfnll(t,params):
        f = params[2]
        tau1 = params[0]
        tau2 = params[1]
        #print(pdf(t,tau1,tau2,f).all() > 0 , tau1, tau2, f)#checking that values stay positive
        nll = -1*(np.log(pdf(t,tau1,tau2,f) + 0.01))#ensuring never taking log of negative number
        return nll
        
    #testval = pdfnll(fi[0],[0.5,0.5,0.5])
    #print ("NLL contribution from val i is " '{}' .format(testval))
    
    yvals = [pdfnll(fi[i],[0.5,0.5,0.5]) for i in range(len(fi))]
    nlltest = np.sum(yvals)
    
    def nll(params,vals):#in the form for scipy optimize
        #f = params[2]
        #tau1 = params[0]
        #tau2 = params[1]
        return np.sum(pdfnll(vals, params))
    

    #bnds = np.array([[0.0001]*3, [float("inf")]*2 + [1] ]).T#no negativity in the parameters
    bnds = np.array([[0.1]*2 + [0], [float("inf")]*2 + [1] ]).T
    #nlltest2= nll(fi,[0.5,0.5,0.5])
    #print ("NLL from whole method is  " '{}' .format(nlltest2))#checking nll method
    #initparams = np.asarray([1,1.5,0.5])
    initparams = np.asarray([0.2,1,0.5])
    
    #NLL = lambda vals,*args: nll(vals,*args)
    Nll = lambda:nll(data, args), 
    #print(nll, type(nll))
    #'L-BFGS-B
    result = minimize(nll,x0=initparams, args=(fi,), bounds=bnds, method='TNC')
    resultdiff = minimize(nll,x0=initparams,args=(fi,),bounds=bnds, method='L-BFGS-B')
    #bounding here to stop f,tau1 and tau2 from going negative
    print("QUESTION 1")
    print("minimizing with the L-BFGS-B Method " '{}' .format(resultdiff.x))
    res = result.x
    print("minimizing with the TNC Method " '{}' .format(res))
    print("====================================")
    tau1opt = res[0]
    tau2opt = res[1]
    fopt = res[2]
    #=================================================================================
    #=====================================QUESTION 2===================================
    #==================================================================================
    print("QUESTION 2")
    #Now for sampling to obtain errors on each parameter
    #cutoffs for sampling t
    t0 =0
    t1 =15*tau2opt#cutoff, means we will be underestimatng for extremely high tvals
    tau1_0 = 0.1
    tau1_1 = 5*tau1opt#cutoff for sampling tau1
    tau2_0 = 0.1
    tau1_1 = 5*tau2opt#cutoff for sampling tau2
    f0 = 0
    f1 = 5*fopt#cutoff for sampling f
    
    valtest1 = pdf(t1,tau1opt,tau2opt,fopt)
    print("Cutoff above which we are not considering a decay is t = " '{}' .format(valtest1))
    
    def maxfun(tauone,tautwo,fnew):#max at t=0
        val = fnew/tauone + (1-fnew)/tautwo
        return val
    def ran(cut1,cut2):#need to scale a random x  variable 
        xval  =  random.random()
        scaledrand=cut1 + (cut2-cut1)*xval
        return scaledrand
        
    def nexttau1(t,tautwo,fnew):#drawing values from distribution for tau1
        #like we did in checkpoint 1 when we sampled for tau
        y2=1.0#to start loop y2>y1
        y1=0.0
        xscal = 0.0
        while y2>y1:
            xscal = ran(tau1_0,tau1_1)
            y1 = pdf(t,xscal,tautwo,fnew)
            y2 = random.random()
            y2 = maxfun(tau1opt,tau2opt,fopt)*y2#scaling y val by optimized function
            if y2<=y1:
                return xscal#scaled tau1 bin val
            else:
                continue 
                
   

    
    
    
    #keeping tautwo and f constant
    #defining lists
    newdata=[]
    tauonelist = []
    #stlist = []
    #now we want to do the previous 'experiment' 500 times
    for i in range (200):
        for j in range (500):
            nextval = nexttau1(fi[0],tau2opt,fopt)#t,tau2,f kept constant when sampling for tau1
            newdata.append(nextval)
            #here calculate tau to get a look at stderr over time
        taunew = np.mean(newdata)
        newdata=[]
        tauonelist.append(taunew)
    
    #tau1tot = np.mean(tauonelist)
    stdevtau1 = np.std(tauonelist)
    print("error on tau1 from parameter searching 3 sigma is = " '{}' .format(stdevtau1))

    #now for tau2===========================================================
    def nexttau2(t,tauone,fnew):#drawing values from distribution for tau2
        #same type of method at nexttau1 - I should have made classes for them
        y2=1.0#to start loop y2>y1
        y1=0.0
        xscal = 0.0
        while y2>y1:
            xscal = ran(tau1_0,tau1_1)
            y1 = pdf(t,tauone,xscal,fnew)
            y2 = random.random()
            y2 = maxfun(tau1opt,tau2opt,fopt)*y2#scaling y val by optimized function
            if y2<=y1:
                return xscal#scaled tau1 bin val
            else:
                continue 


    tautwolist = []
    #stlist = []
    #now we want to do the previous 'experiment' 500 times
    for i in range (200):
        for j in range (500):
            nextval = nexttau2(fi[0],tau1opt,fopt)#t,tau1,f kept constant when sampling for tau2
            newdata.append(nextval)
            #here calculate tau to get a look at stderr over time
        tautwonew = np.mean(newdata)
        newdata=[]
        tautwolist.append(tautwonew)
    
    stdevtau2 = np.std(tautwolist)
    print("error on tau2 from parameter searching 3 sigma is = " '{}' .format(stdevtau2))


    #now for sigma f===============================================

    def nextf(t,tauone,tautwo):#drawing values from distribution for tau2
        #same type of method at nexttau1 and nexttau2 - I should have made classes for them
        y2=1.0#to start loop y2>y1
        y1=0.0
        xscal = 0.0
        while y2>y1:
            xscal = ran(f0,f1)
            y1 = pdf(t,tauone,tautwo,xscal)
            y2 = random.random()
            y2 = maxfun(tau1opt,tau2opt,fopt)*y2#scaling y val by optimized function
            if y2<=y1:
                return xscal#scaled tau1 bin val
            else:
                continue 


    flist = []
    #stlist = []
    #now we want to do the previous 'experiment' 500 times
    for i in range (200):
        for j in range (500):
            nextval = nextf(fi[0],tau1opt,tau2opt)#t,tau1,tau2 kept constant when sampling for f
            newdata.append(nextval)
            #here calculate tau to get a look at stderr over time
        fnew = np.mean(newdata)
        newdata=[]
        flist.append(fnew)
    
    stdevf = np.std(flist)
    print("error on f from parameter searching 3 sigma is = " '{}' .format(stdevf))


    #now plotting NLL with +- 3sigma


    xtauone = np.linspace((tau1opt - 3*stdevtau1),(tau1opt + 3*stdevtau1))
    #rescaling
    #for i in range(len(xtauone)):
    #    xtauone[i] = xtauone[i]/(tau1opt)
    ytauone = np.zeros(len(xtauone))
    xtautwo = np.linspace((tau2opt - 3*stdevtau2),(tau2opt + 3*stdevtau2))
    ytautwo = np.zeros(len(xtautwo))
    
    xf = np.linspace((fopt - 3*stdevf),(fopt + 3*stdevf))
    yf = np.zeros(len(xf))
    #=============================================================================
    tauonebaseval = tau1opt - 3*stdevtau1
    step = xtauone[1]-xtauone[0]
    for i in range(len(xtauone)):
        ytauone[i] = nll([tauonebaseval,tau2opt,fopt],fi)
        tauonebaseval = tauonebaseval + step
        #print(tauonebaseval)
        
    '''
    plt.plot(xtauone,ytauone)
    plt.xlabel("Tau one")
    plt.ylabel("Negative Log Likelihood")
    plt.title("Negative Log Likelihood as Tau two varies around mean")
    plt.show()
    '''

    #==============================================================================    
    tautwobaseval = tau2opt - 3*stdevtau2
    step2 = xtautwo[1]-xtautwo[0]
    for i in range(len(xtautwo)):
        ytautwo[i] = nll([tau1opt,tautwobaseval,fopt],fi)
        tautwobaseval = tautwobaseval + step
        #print(tautwobaseval)


    '''
    plt.plot(xtautwo,ytautwo)
    plt.xlabel("Tau two")
    plt.ylabel("Negative Log Likelihood")
    plt.title("Negative Log Likelihood as Tau two varies around mean")
    plt.show()
    '''
    #===============================================================================
    fbaseval = fopt - 3*stdevf
    stepf = xf[1]-xf[0]
    for i in range(len(xf)):
        yf[i] = nll([tau1opt,tau2opt,fbaseval],fi)
        fbaseval = fbaseval + stepf
        #print(fbaseval)
    print("====================================")

    '''
    plt.plot(xf,yf)
    plt.xlabel("Fraction f")
    plt.ylabel("Negative Log Likelihood")
    plt.title("Negative Log Likelihood as Fraction f varies around mean")
    plt.show()
    '''
    #================================================================================
    #================================================================================
    #=====================================QUESTION3==================================
    #================================================================================
    #================================================================================
    print("QUESTION 3")
   
    
    #method for going up NLL
    def checkertau1(toler):
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevtau1*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on tauaxis
        #flip = 0
        nllvaltest = 2*nllvalwant
        diff = nllvalwant - nllvaltest
        while abs(guessstep) > toler:
        #for i in range(100):
            nllvaltest = nll([tau1opt+guessstep,tau2opt,fopt],fi)
            howfar += guessstep
            if nllvaltest > nllvalwant:
                guessstep = -guessstep*0.5
                flip = 1#means it's going backwards
            elif  nllvaltest < nllvalwant:
                guessstep = -guessstep*0.5
                flip = 0#now back to forwards
            #print (guessstep)
        return howfar#distance moved in the parameter axis
    
    errortau1 = checkertau1(0.000001)
    print ("error on tau1 from increasing NLL by 0.5 is " '{}' .format(errortau1))
    #======================================================================

    def checkertau2(toler):
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevtau2*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on tauaxis
        #flip = 0
        nllvaltest = 2*nllvalwant
        diff = nllvalwant - nllvaltest
        while abs(guessstep) > toler:
        #for i in range(100):
            nllvaltest = nll([tau1opt,tau2opt+guessstep,fopt],fi)
            howfar += guessstep
            if nllvaltest > nllvalwant:
                guessstep = -guessstep*0.5
                flip = 1#means it's going backwards
            elif  nllvaltest < nllvalwant:
                guessstep = -guessstep*0.5
                flip = 0#now back to forwards
            #print (guessstep)
        return howfar#distance moved in the parameter axis
    
    errortau2 = checkertau2(0.000001)
    print ("error on tau2 from increasing NLL by 0.5 is " '{}' .format(errortau2))
    

    #=====================================================================
    #======================================================================

    def checkerf(toler):
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevf*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on faxis
        #flip = 0
        nllvaltest = 2*nllvalwant
        diff = nllvalwant - nllvaltest
        while abs(guessstep) > toler:
        #for i in range(100):
            nllvaltest = nll([tau1opt,tau2opt,fopt+guessstep],fi)
            howfar += guessstep
            if nllvaltest > nllvalwant:
                guessstep = -guessstep*0.5#go backwards smaller step
            elif  nllvaltest < nllvalwant:
                guessstep = -guessstep*0.5#go forwards smaller step
            #print (guessstep)
        return howfar#distance moved in the parameter axis
    
    errorf = checkerf(0.000001)
    print ("error on f from increasing NLL by 0.5 is " '{}' .format(errorf))
    
    print("=========================================")
    #=========================================================================
    #=========================================================================
    #=========================================================================
    #=========================================================================
    #===============================Question 4================================
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #here we are drawing t from the fitted distribution
    print("QUESTION 4")
    def nextt(tauone,tautwo,fnew):#drawing values from distribution for t
        y2=1.0#to start loop y2>y1
        y1=0.0
        xscal = 0.0
        while y2>y1:
            xscal = ran(t0,t1)
            y1 = pdf(xscal,tauone,tautwo,fnew)
            y2 = random.random()
            y2 = maxfun(tau1opt,tau2opt,fopt)*y2#scaling y val by optimized function
            if y2<=y1:
                return xscal#scaled t bin val
            else:
                continue 
                
    tlist = []
    #stlist = []
    #now we want to do the previous 'experiment' 500 times
    for i in range (200):
        for j in range (500):
            nextval = nextt(tau1opt,tau2opt,fopt)
            newdata.append(nextval)
        tnew = np.mean(newdata)
        newdata=[]
        tlist.append(tnew)
    meant = np.mean(tlist)
    stdevt = np.std(tlist)
    print("Mean t = " '{}' " and stdev of t is "'{}' .format(meant,stdevt))
    print("observed t = " '{}' .format(meanobst))
    
    xvalplot = np.linspace(0,7,100)
    yvalplot = np.zeros(len(xvalplot))
    for i in range(len(xvalplot)):
        yvalplot[i]=pdf(fi[i],tau1opt,tau2opt,fopt)
        
    plt.hist(fi,bins=100)
    plt.hist(yvalplot)
    plt.show()
    #plt.plot(xvalplot,yvalplot)
    #plt.show()

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
