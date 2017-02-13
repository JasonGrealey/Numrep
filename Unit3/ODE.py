import random
import math as mth
import numpy as np

class Res:
    #initialising results list
    def __init__(self):
        self.results = []
    def app(self,coord):
        self.results.append(coord)
    def get(self,a):
        if ((i<0) or (i>len(self.results))):
            print ('error, index not in range')
            return [0.,0.]
        return self.results[a]
    def retall(self):
        return self.results
    def yvals(self):
        yvals = [y for [x,y] in self.results ]
        return yvals
    def xval(self):
        xvals = [x for [x,y] in self.results ]
        return xvals
        
#===========================================================
#here we are creating a class for exponential 

class ODEExp():
    #exponential code y'=y*k
    def __init__(self,_k):
        self.k=_k
        #getting initial coordinates
        self.initvals = [self.exactsoln(0.),0. ]
    def firstderiv(self, coords):
        #multiplying y by k when derivative note (x,y)
        return self.k*coords[1]
        #returning initial coordinates
    def ival(self):
        return self.ival
        #returning the exact value of y
    def exactsoln(self,x):
        return mth.exp(self.k * x)

#=============================================================

class ODEPoly():
    #polynomial code
    def __init__(self,_coeffs):
        self.coeffs=_coeffs
        #getting initial coordinates
        self.initvals = [self.exactsoln(0.),0. ]
    def firstderiv(self, coords):
        #derivative of polynomial here
        valder = 0
        #looping 4 times, and matching coefficients properly (skipping 0th term)
        for power in range(len(self.coeffs)-1):
            valder+= (power+1)*self.coeffs[power+1]*mth.pow(coords[0], float(power))
        return valder
        #returning initial coordinates
    def ival(self):
        return self.ival
        #returning the exact value of y
    def exactsoln(self,x):
        val = 0
        for power in range(len(self.coeffs)):
            val+= self.coeffs[power]+mth.pow(x,float(power))

#=============================================================

class ODESinusoid():
    def __init__(self,omega):
        print ('creating wave')
        self.omega=omega
        self.initial = [self,exactsoln(0.),0.]
        
    def firstderiv(self,coords):
        return self.omega * mth.cos(self.omega*coords[0])
    def ival(self):
        return self.inital
    def exactsoln(self,x):
        return sin(self.omega*x)

#=============================================================

class StepEuler:
    def dy(self,ode,coords,dx):
        dy =ode.firstderiv(coords)*dx
        return [dy,dx]

class StepRK:
    def dy(self,ode,pair,dx):
        x = coord[0]
        y = coord[1]
        d1 = ode.firstderiv( [x,y] )
        d2 = ode.firstderiv( [x+dx/2,y+(dx/2)*d1 ] )
        d3 = ode.firstderiv( [x+dx/2,y+(dx/2)*d2] )
        d4 = ode.firstderiv( [x+dx,y+dx*d3] )
        dy = dx*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
        return [ dy, dx ]

class StepRK0:
    def dy(self,ode,pair,dx):
        mid = [pair[0]+dx/2, pair[1]+ode.firstderiv(pair)* (dx/2)]
        dy = ode.firstderiv(mid) * dx
        return[dx,dy]




