import numpy as np
import math
import matplotlib.pyplot as plt

#here we are writing some code to plot the functions
#result lists
bipres= []
bisres=[]
bieres = []
nrpres = []
nrsres = []
nreres = []
secpres = []
seceres=[]
secsres=[]

#10.2 -7.4x -2.1x^2 +x^3
#e^x - 2
#cos(X)sin(3s)
def main():
    class poly():
        def __init__(self,_coeffs):
            self.coeffs = _coeffs
        def val(self,x):
            val=0
            for power in range(len(self.coeffs)):
                val+= self.coeffs[power]*math.pow(x,float(power))
            return val
        def der(self,x):
            valder = 0
            for power in range(len(self.coeffs)-1):
                valder+= (power+1)*self.coeffs[power+1]*math.pow(x, float(power))
            return valder
    class sincos():
        def __init__(self,ksin,kcos):
            self.ksin=ksin
            self.kcos=kcos
        def val(self,x):
            return (math.cos(self.kcos*x))*(math.sin(self.ksin*x))
        def der(self,x):
            return (-(1.0)*self.kcos*(math.sin(self.kcos*x))*(math.sin(self.ksin*x)) + self.ksin*((math.cos(self.kcos*x))*(math.cos(self.ksin*x))))
    class exp():
        def __init__(self,k,consta):
            self.k=k
            self.consta=consta
        def val(self,x):
            return (np.exp(x*self.k) + self.consta)
        def der(self,x):
            return (self.k*(np.exp(x*self.k)))

    '''
    '''
    #now for the real functions
    sincos = sincos(3,1)#[sin,cos]
    expon = exp(2,-1)#[k,const]
    poly = poly([10.2,-7.4,-2.1,1])#[const,x^1...x^n]
    xvalpol = np.linspace(-3,4)
    xvale = np.linspace(-1,0.3)
    xvalsi = np.linspace(-1.5,2)
    
    #print(xvalues)
    ysin = []
    ypoly = []
    yexp = []
    for i in range(len(xvalpol)):#they have same range
        ysin.append(sincos.val(xvalsi[i]))
        ypoly.append(poly.val(xvalpol[i]))
        yexp.append(expon.val(xvale[i]))
    
    #  for i in len(xvalues)
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(xvalpol, ypoly)
    plt.title('poly')

    plt.subplot(222)
    plt.plot(xvale, yexp)
    plt.title('exp')

    plt.subplot(223)
    plt.plot(xvalsi, ysin)
    plt.title('sincos')
    
    plt.show()
    
    xvals = []
    def sign(a, b):#ret true if same sign, false otherwise
        return( a * b > 0)


    def intervalfinder(start,finish,steps,function):
        lista=[]#storing results of finding intervals
        length = float(abs(start-finish))#size of sample space
        steplen = float(length/steps)#size of steps
        temp = []#here make temporary list of xvalues
        tempnew=[]#here making a temp list of results
        val=0
        for i in range(steps):#calculating values of function
            temp.append(function.val(start+val))
            val+=steplen
            #print(str(function))
        for i in range(steps -1):#checking for changes of sign in this range
            a=temp[i]
            b=temp[i+1]
            #print (sign(a,b))
            #print (a , b)
            if (sign(a,b)) == False :
                #print (str(function))
                #print("here")
                tempnew.append(start+(i)*steplen)#appending xvalues for a
                tempnew.append(start+(i+1)*steplen)#appending xvalues for b
                lista.append(tempnew)
                tempnew=[]
            else: 
                continue
        temp=[]
        return lista
    
    def Bisection(x1, x2, toler,function):
        xmid = (x2+x1)/2
        #err = abs(x2-x1)
        nstep = 1
        nstepmax = 90
        for i in range(nstepmax): # limit iterations to prevent infinite loop
            mid = (x1+ x2)/2 # new midpoint
            if function.val(mid) == 0 or abs((x2 - x1)/2) < toler: # solution found
                return mid
            elif sign(function.val(mid),function.val(x1)) == True: 
                #here we change a to c or b to c depending on sign(aorb)==sign(c)
                x1 = mid #chance old midpoint to new leftpoint
            else:
                x2 = mid # new interval
        #print("not reached thresh")
        return xmid
   
    #intervals calculated
    pinter = intervalfinder(-3,4,20,poly)
    einter = intervalfinder(-1,3,10,expon)
    sinter = intervalfinder(-1.5,2,20,sincos)#10 steps isn't enough for NR poly

    def NR(function, x0, toler):
        lastX = x0
        nextX = lastX + 1* toler  # "different than lastX so loop starts OK
        while (abs(lastX - nextX) > toler):  # this is how you terminate the loop - note use of abs()
            newY = function.val(nextX)                     # just for debug... see what happens
            #print ("f(", nextX, ") = ", newY)     # print out progress... again just debug
            lastX = nextX
            nextX = lastX - newY / function.der(lastX)  # update estimate using N-R
        return nextX

    def secant(function,x0,x1, toler,nstep):
        n=0
        while n<=nstep:
            n+=1
            x2 = x1 - function.val(x1)*((x1-x0)/(function.val(x1)-function.val(x0)))
            if abs(x2-x1) <= toler:
                return x2
            else:
                x0 = x1
                x1 = x2
        return False

    def pclarke(x0,x1,function,toler):
         xs = x1 - function.val(x1)*((x1-x0)/(function.val(x1)-function.val(x0)))
         xmid = (x0+x1)/2
         if xs <= x1 or xs <=x0:
             #inrange
             x2=xs
             if sign(function.val(x2),function.val(x1)) == True: 
                #here we change a to c or b to c depending on sign(aorb)==sign(c)
                x1 = x2 #chance old midpoint to new leftpoint
             else:
                x0 = x2 # new interval
            
         else:
             x2 = xmid
             if sign(function.val(x2),function.val(x1)) == True: 
                #here we change a to c or b to c depending on sign(aorb)==sign(c)
                x1 = x2 #chance old midpoint to new leftpoint
             else:
                x0 = x2 # new interval
             

   
    #here running for the amount of crosses the bisection algorithm
    tol = 0.00001
    for i in range(len(pinter)):
        bipres.append(Bisection(pinter[i][0],pinter[i][1],tol,poly))
        nrpres.append(NR(poly,pinter[i][0],tol))
        secpres.append(secant(poly,pinter[i][0],pinter[i][1],tol,100))
    print(bipres)#correct
    print (nrpres) 
    print(secpres)
    
    for i in range(len(einter)):
        bisection = Bisection(einter[i][0],einter[i][1],tol,expon)
        #bieres.append(Bisection(einter[i][0],einter[i][1],0.0000001,expon))
        bieres.append(bisection)
        nreres.append(NR(expon,einter[i][0],tol))
        seceres.append(secant(expon,einter[i][0],einter[i][1],tol,100))
    print(bieres)
    print(nreres)
    print(seceres)
    
    for i in range(len(sinter)):
        bisres.append(Bisection(sinter[i][0],sinter[i][1],tol,sincos))
        nrsres.append(NR(sincos,sinter[i][0],tol))
        secsres.append(secant(sincos,sinter[i][0],sinter[i][1],tol,100))

    print(bisres)
    print(nrsres)
    print(secsres)
    exit()

main()
