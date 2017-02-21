import numpy as py
import math as mth
from ODE import *
import matplotlib.pyplot as plt
from scipy import optimize

def main():
    height = 10
    ode = ODEefield(height)
    #nsteps = int( input( "Enter number of steps ") )
    delta = float (input( "Enter step size "))
    nsteps = int(4.0/delta)
    #printcheck
    print ("Running with  nsteps = %d and dx = %d" % ( nsteps, delta))
    #creating the Euler step
   # print("pre euler step")
    eulermethod=StepEuler( )
    eulerperform=perform(ode,eulermethod, ' Euler integration')
   # print("does it make it here?")
    
    rk2method=StepRK2( )
    rk2perform=perform(ode,rk2method, '  RKmidpoint integration')
    
    rk4method=StepRK4( )
    rk4perform=perform(ode,rk4method, ' RK4 intergration')
    
    #running 
    eulerres= eulerperform.run(nsteps,delta)
    print("Euler method has run")
    rk2res= rk2perform.run(nsteps,delta)
    print("RK2 method has run")
    rk4res= rk4perform.run(nsteps,delta)
    print("RK4 method has run")
    
    yvaleul = eulerres.yvals()
    yvalrk2 = rk2res.yvals()
    yvalrk4 = rk4res.yvals()
    xvals = rk4res.xvals()
   # print(len(yvaleul))
   # print(len(xvals))
   # yexact = [ode.exactsoln(coords[0]) for coords in eulerres.retall()]

  #  def piecewise_linear(x,x0,x1,y0,y1,k1,k2,k3):
   #     return np.piecewise(x, [x < x0,(x0<=x) & (x<x1),x>=x1], [lambda x:k1*x + y0-k1*x0, lambda x: height *mth.sin(x*x1 +k2)+y1-k2*x1, lambda x: k3*x + y0 -k3*x1])
    #popt, fit = curve_fit(piecewise_linear,xvals,yvaleul)
   # polyfit =np.poly1d(np.polyfit(xvals, yvaleul, 7))
    def piecewise(x,x0,a,b,c,d,x1):
        return( np.piecewise(x,[x<1,(1<=x) & (x<=3.5),x>=3.5],[lambda x: x0, lambda x: a*np.sin(b*x + c)+d, lambda x:x1]))
    l, pcov = optimize.curve_fit(piecewise,xvals,yvaleul,p0 = [0,height,1,1,1,0])
    
    print (l)
    print(np.sqrt(np.diag(pcov)))
   # p , e = optimize.curve_fit(piecewise_linear, xvals, yvaleul)#, p0=[1,2,1,1,1,1,1])
    xd = np.linspace(0, 4, 100)
    #plt.plot(x, y, "o") 
                # plt.plot(polyfit)

    plt.plot(xvals,yvaleul)
    plt.plot(xvals,yvalrk2)
    plt.plot(xvals,yvalrk4)
   # plt.plot(xvals,yexact)
    plt.legend(['Euler', 'RK2', 'RK4', 'Exact'], loc='upper left')
    plt.title("Electric field")
    plt.show()
    
    #here are plotting a piecewise sinusoidal fit of the first integration (efield)
    plt.xlim(0,4)
    plt.plot(xvals,yvaleul)
    plt.plot(xd, piecewise(xd, *l))
    plt.legend(['Euler data ', 'Sinusoidal plot for for next integration'], loc='upper left')
    plt.show()





    #here we are initalising a sinusoid (omega,height,phase,start point,endpoint)
    newode = ODESinusoid(2.6,6.3,-2.8,0.5,4)
   # newnsteps = int( input( "Enter number of steps for second integration ") )
    newdelta = float (input( "Enter step size for second integration "))
       # delta = float (input( "Enter step size "))
    newnsteps = int(4.0/newdelta)
    neweulermethod=StepEuler( )
    neweulerperform=perform(newode,neweulermethod, 'second Euler integration')
   # print("does it make it here?")
    
    newrk2method=StepRK2( )
    newrk2perform=perform(newode,newrk2method, 'second  RKmidpoint integration')
    
    newrk4method=StepRK4( )
    newrk4perform=perform(newode,newrk4method, 'second  RK4 intergration')
    
    #running 
    neweulerres= neweulerperform.run(newnsteps,newdelta)
    print("Euler method has run for the second time")
    newrk2res= newrk2perform.run(newnsteps,newdelta)
    print("RK2 method has run for the second time")
    newrk4res= newrk4perform.run(newnsteps,newdelta)
    print("RK4 method has run for the second time")
    print(l[0])
    #now for calculating v using new ode
    newyvaleul = neweulerres.yvals()
    newyvalrk2 = newrk2res.yvals()
    newyvalrk4 = newrk4res.yvals()
    print(newyvaleul)
    #here we are ensuring we get the negative sign correctly and adding the onset calulated from the fitting function
    for i in range(len(newyvaleul)):
        newyvaleul[i]=-(1.0)*newyvaleul[i] -0.25
        newyvalrk2[i]=-(1.0)*newyvalrk2[i] -0.25
        newyvalrk4[i]=-(1.0)*newyvalrk4[i] -0.25
    print(newyvaleul)
    newxvals = newrk4res.xvals()
    plt.plot(newxvals,newyvaleul)
    plt.plot(newxvals,newyvalrk2)
    plt.plot(newxvals,newyvalrk4)
   # plt.plot(xvals,yexact)
    plt.legend(['Euler', 'RK2', 'RK4'], loc='upper left')
    plt.title("Potential")
    plt.show()
        
    
main()
