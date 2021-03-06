import random
import math
import numpy as np

class Res:
    #initialising results list
    def __init__(self):
        self.results = [ ]
    def app(self,coords):
        self.results.append(coords)
    def get(self,a):
        if ((a<0) or (a>len(self.results))):
            print ('error, index not in range')
            return [0.,0.]
        return self.results[a]
    def retall(self):
        return self.results
    def yvals(self):
        yvals = [y for [x,y] in self.results ]
        return yvals
    def xvals(self):
        xvals = [x for [x,y] in self.results ]
        return xvals
    def printit(self):
        print (self.results)
        
#===========================================================
#here we are creating a class for exponential 

class ODEExp():
    #exponential code y'=y*k
    def __init__(self,_k):
        self.k=_k
        print("initialising ODE exponential")
        self.ival = [0. , self.exactsoln(0.)]

    def ival(self):
        return self.ival
        
    def firstderiv(self, coords):
        #multiplying y by k when derivative note (x,y)
       # coords=[1,1]
       # coords.append(1)
       # coords.append(1)
       # print("lolololol")
       # print (len(coords))
        return (self.k*(coords[1]))
        #returning initial coordinates
        #returning the exact value of y
    def exactsoln(self,x):
        return math.exp(self.k*x)

#=============================================================

class ODEPoly():
    #polynomial code
    def __init__(self,_coeffs):
        self.coeffs=_coeffs
        #getting initial coordinates
        self.ival = [-0., self.exactsoln(-0.)]
    def firstderiv(self, coords):
        #derivative of polynomial here
        valder = 0.
        #looping 4 times, and matching coefficients properly (skipping 0th term)
        for power in range(len(self.coeffs)-1):
            valder+= (power+1)*self.coeffs[power+1]*math.pow(coords[0], float(power))
        return valder
        #returning initial coordinates
    def ival(self):
        return self.ival
        #returning the exact value of y
    def exactsoln(self,x):
        val = 0
        for power in range(len(self.coeffs)):
            val+= self.coeffs[power]+math.pow(x,float(power))
        return val

#=============================================================

class ODESinusoid():
    def __init__(self,omega,a,c,start,end):
        print ('creating wave')
        self.omega=omega
        self.a=a
        self.c=c
        self.start=start
        self.end=start
        self.ival = [0. , self.exactsoln(0.)]
        
    def firstderiv(self,coords):
        if coords[0]<self.start:
            return 0.
        elif coords[0]>self.end:
            return 0.
        else:
            return (self.omega*self.a * math.cos(self.omega*coords[0]+self.c))

    def ival(self):
        return self.ival
        #here we are only evaluating the parts of the sinusoid present from the first integration ensureing that it is 0 when supposed to be
    def exactsoln(self,x):
        if x< self.start:
            return 0.
        elif x> self.end:
            return 0.
        else:
            return ((self.a)*(math.sin(self.omega*x+self.c)))
#=============================================================

class ODEefield():
    def __init__(self,height):
        print("making ODE for Electric field")
        self.height = height
        self.ival = [0.,self.exactsoln(0.)]
    
    def firstderiv(self,coords):
        if 0.999 <= coords[0] <= 1.001:
            return (self.height)
        elif 1.99 <= coords[0] <= 2.001:
            return (-2.0 *self.height)
        elif 2.99 <= coords[0] <= 3.001:
            return (self.height)
        else:
            return 0.
    def ival(self):
        return self.ival
        #here we are defining the heaviside density
 #   def exactsoln(self,x):
  #      if x<0 or x>4:
   #         print("x must be positive and in the range 0->4")
    #        quit()
     #   elif 0 <= x <= 1:
      #      return (0.)
       # elif 1 <= x <= 2:
   #         return (self.height)
    #    elif 2 <= x <= 3:
     #       return (-1.0 *self.height)
      #  elif 3 <= x <= 4:
       #     return (0.)
    def exactsoln(self,x):
        if 0<=x<=4:
            return(  np.piecewise(x, [0<=x <= 1,1<= x <=2,2<=x<=3,3 <= x <= 4], [0.,self.height,(-1.0) *(self.height),0.]))
        else:
            print("x must be positive and in the range 0->4")
            quit()

#=============================================================

class StepEuler:
    def dy(self,ode,coords,dx):
       # print("euler method working")
        dy = ode.firstderiv(coords)*dx
       # print("euler method finished for one")
        return [dx,dy]

class StepRK4:
    def dy(self,ode,coords,dx):
       # print("STEP RK FULL ")
        x = coords[0]
        y = coords[1]
        d1 = ode.firstderiv( [x,y] )
        d2 = ode.firstderiv( [x+dx/2,y+dx/2*d1 ] )
        d3 = ode.firstderiv( [x+dx/2,y+dx/2*d2] )
        d4 = ode.firstderiv( [x+dx,y+dx*d3] )
        dy = dx*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
        return [ dx, dy ]

class StepRK2:
    def dy(self,ode,coords,dx):
       # print (" step rk0 ")
        mid = [coords[0]+dx/2, coords[1]+ode.firstderiv(coords)* (dx/2)]
        dy = ode.firstderiv(mid) * dx
        return[dx,dy]
#===============================================================

class perform:
    def __init__(self,ode,step,name):
        self.ode=ode
        self.step=step
        self.name=name
        #this method calculates the actual results given stepsize and #steps
    def run(self,nsteps,dx):
        res = Res()
        #HERE IS A PROBLEM
        res.app(self.ode.ival)
        print("checking iniial values")
        res.printit()
        #integration loop
        for i in range (nsteps):
            now = res.get(i)#step here is defining dy from the class we need
            #here edlta is the step from now to new using method, ode and dx size
            delta = self.step.dy(self.ode, now, dx)
            new = [now[0]+delta[0], now[1]+delta[1]]
            res.app(new)
            
        print (("method finished for %s") %( self.name))
        print("checking final results")
        res.printit()
        return res
    



