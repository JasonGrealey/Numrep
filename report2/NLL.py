# first we shall import the data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import random

def main():
    filename = "DecayTimesData.txt"
    fi = np.loadtxt(filename)
    meanobst = np.mean(fi)
    stdevobst = np.std(fi)
    def normfactor(cut,tau1,tau2,f):#determing by how much of pdf we need to normlaise due to cutoff
        val =1/(1- np.exp(-cut/tau2) - f*(np.exp(-cut/tau1) - np.exp(-cut/tau2)))
        return(val)
    def pdf(t,tau1,tau2,f):
        val = f*(1/tau1)*np.exp(-(t/tau1)) + (1-f)*(1/tau2)*np.exp(-(t/tau2))*1.00949845061#this normalises the pdf
        return val
    def pdfnll(t,params):
        f = params[2]
        tau1 = params[0]
        tau2 = params[1]
        val = pdf(t,tau1,tau2,f)
        if np.any(val)<=0:#at some points during optimisation the pdf may be negative so we must ignore these values 
            nll = 0
            return nll
        else:
            #nll = -1*(np.log(pdf(t,tau1,tau2,f) + 0.00001))#ensuring never taking log of negative number
            nll = -1*(np.log(pdf(t,tau1,tau2,f)))
            return nll
    def nll(params,vals):#in the form for scipy optimize
        return np.sum(pdfnll(vals, params))
    bnds = np.array([[0.0001]*3, [float("inf")]*2 + [1] ]).T#no negativity in the parameters
    #bounding here to stop f,tau1 and tau2 from going negative
    initparams = np.asarray([3,5,0.5])
    Nll = lambda:nll(data, args), 
    result = minimize(nll,x0=initparams, args=(fi,), bounds=bnds, method='TNC')
    print("QUESTION 1")
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
    cutoff = 9.578530184172956e-08 #Probability of pdf getting past cutoff t1
    tet = normfactor(t1,0.18,0.84,0.73)
    #print(tet)#this factor was calculated to normalise it
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
    for i in range (200):
        for j in range (500):
            nextval = nextf(fi[0],tau1opt,tau2opt)#t,tau1,tau2 kept constant when sampling for f
            newdata.append(nextval)
        fnew = np.mean(newdata)
        newdata=[]
        flist.append(fnew)
    stdevf = np.std(flist)
    print("error on f from parameter searching 3 sigma is = " '{}' .format(stdevf))


    #now plotting NLL with +- 3sigma


    xtauone = np.linspace((tau1opt - 3*stdevtau1),(tau1opt + 3*stdevtau1))
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
    plt.plot(xtauone,ytauone)
    plt.xlabel("Tau one", fontsize=20)
    plt.ylabel("Negative Log Likelihood", fontsize=20)
    plt.title("Negative Log Likelihood as Tau one varies around mean", fontsize=20)
    plt.show()
    #==============================================================================    
    tautwobaseval = tau2opt - 3*stdevtau2
    step2 = xtautwo[1]-xtautwo[0]
    for i in range(len(xtautwo)):
        ytautwo[i] = nll([tau1opt,tautwobaseval,fopt],fi)
        tautwobaseval = tautwobaseval + step
    plt.plot(xtautwo,ytautwo)
    plt.xlabel("Tau two", fontsize=20)
    plt.ylabel("Negative Log Likelihood", fontsize=20)
    plt.title("Negative Log Likelihood as Tau two varies around mean", fontsize=20)
    plt.show()
    #===============================================================================
    fbaseval = fopt - 3*stdevf
    stepf = xf[1]-xf[0]
    for i in range(len(xf)):
        yf[i] = nll([tau1opt,tau2opt,fbaseval],fi)
        fbaseval = fbaseval + stepf
    print("====================================")
    plt.plot(xf,yf)
    plt.xlabel("Fraction f", fontsize=20)
    plt.ylabel("Negative Log Likelihood", fontsize=20)
    plt.title("Negative Log Likelihood as Fraction f varies around mean", fontsize=20)
    plt.show()
    #================================================================================
    #================================================================================
    #=====================================QUESTION3==================================
    #================================================================================
    #================================================================================
    print("QUESTION 3")
    #method for going up NLL
    def checkertau1(toler):#this method check how much you vary tau1
        #to move the NLL by 0.5 from minimum
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevtau1*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on tauaxis
        nllvaltest = 2*nllvalwant#guess
        diff = nllvalwant - nllvaltest
        while abs(guessstep) > toler:
        #for i in range(100):
            nllvaltest = nll([tau1opt+guessstep,tau2opt,fopt],fi)
            howfar += guessstep
            if nllvaltest > nllvalwant:
                guessstep = -guessstep*0.5
            elif  nllvaltest < nllvalwant:
                guessstep = -guessstep*0.5
        return howfar#distance moved in the parameter axis
    
    errortau1 = checkertau1(0.000001)
    print ("error on tau1 from increasing NLL by 0.5 is " '{}' .format(errortau1))
    #======================================================================

    def checkertau2(toler):#this method check how much you vary tau2
        #to move the NLL by 0.5 from minimum
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevtau2*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on tauaxis
        nllvaltest = 2*nllvalwant#guess
        diff = nllvalwant - nllvaltest
        while abs(guessstep) > toler:
        #for i in range(100):
            nllvaltest = nll([tau1opt,tau2opt+guessstep,fopt],fi)
            howfar += guessstep
            if nllvaltest > nllvalwant:
                guessstep = -guessstep*0.5
            elif  nllvaltest < nllvalwant:
                guessstep = -guessstep*0.5
        return howfar#distance moved in the parameter axis
    
    errortau2 = checkertau2(0.000001)
    print ("error on tau2 from increasing NLL by 0.5 is " '{}' .format(errortau2))
    

    #=====================================================================
    #======================================================================

    def checkerf(toler):#this method check how much you vary f
        #to move the NLL by 0.5 from minimum
        nllvalmean =  nll([tau1opt,tau2opt,fopt],fi)#calculate at mean
        nllvalwant = nllvalmean + 0.5 #value we want
        guessstep = stdevf*2 #big step to move tau1
        howfar =0 #tracking how far we are moving on faxis
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
            xscal = ran(t0,t1)#scaled random xval 
            y1 = pdf(xscal,tauone,tautwo,fnew)
            y2 = random.random()
            y2 = maxfun(tau1opt,tau2opt,fopt)*y2#scaling y val by optimized function
            if y2<=y1:
                return xscal#scaled t bin val
            else:
                continue 
    tlist = []
    for i in range (200):
        for j in range (500):#performing 200 experiments of 500 decays
            nextval = nextt(tau1opt,tau2opt,fopt)#nextt draws t from optimized pdf
            newdata.append(nextval)
        tnew = np.mean(newdata)
        newdata=[]
        tlist.append(tnew)
    meant = np.mean(tlist)
    stdevt = np.std(tlist)
    print("Mean t = " '{}' " and stdev of t is "'{}' .format(meant,stdevt))
    print("observed t = " '{}' " and stdev of t in experiment is = " '{}' .format(meanobst,stdevobst))
    
    
    #printing how far values are from experiment
    xvalplot = np.linspace(0,max(fi),100)
    yvalplot = np.zeros(len(fi))
    for i in range(len(fi)):
        yvalplot[i]=pdf(fi[i],tau1opt,tau2opt,fopt)
    withinexp = abs(meant-meanobst)/stdevobst
    print("within " '{}' " standard deviations of experimental error".format(withinexp))
    withinsim = abs(meant-meanobst)/stdevt
    print("within " '{}' " standard deviations of simulated error".format(withinsim))

    #plotting the normalised histogram against optomized pdf
    xval = np.linspace(0,7,100)
    yval = [pdf(xval[i],tau1opt,tau2opt,fopt) for i in range(len(xval))]
    plt.plot(xval,yval,linewidth=3)
    plt.hist(fi,bins=100,normed=True)#normalise so pdf will fit properly
    #plt.hist(fi,bins=100)
    plt.xlabel("Decay Time", fontsize=20)
    plt.ylabel("Normalised Counts and Optimized PDF", fontsize=20)
    plt.title("The Normalised Experimental Histogram vs The Optimized PDF", fontsize=20)
    plt.show()

    plt.hist(fi,bins=50)
    plt.xlabel("Decay Time", fontsize=20)
    plt.ylabel("Counts of Decays", fontsize=20)
    plt.title("Experimental Decays as a Histogram", fontsize=20)
    #plt.plot(xvalplot,yvalplot)
    plt.show()
    #apologies for making the code long, hopefully it is still readable. 
main()
