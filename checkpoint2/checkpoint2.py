import numpy as py
import math as mth
from ODE import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def main():
    
    ode = ODEefield(10.)
    #nsteps = int( input( "Enter number of steps ") )
    delta = float (input( "Enter step size "))
    nsteps = int(4.0/delta)
    #printcheck
    print ("Running with  nsteps = %d and dx = %d" % ( nsteps, delta))
    #Create ODE
    
        # poly = ODEPoly([1.0,2.0,3.0,4.0])
        #print(poly.firstderiv([1.0,1.0]))
    
        # expon = ODEExp(5.0)
        # print(expon.firstderiv([10.0,10.0]))
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
    
   # yexact = [ode.exactsoln(coords[0]) for coords in eulerres.retall()]
 #   plt.plot(x, x)
  #  plt.plot(x, 2 * x)
   # plt.plot(x, 3 * x)
    #plt.plot(x, 4 * x)

    def piecewise_linear(x, x0, y0, k1,k2,k3,k4):
        return (np.piecewise(x, [x < x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0, lambda x:k3*x + y0-k3*x0, lambda x:k4*x + y0-k4*x0]))
    popt, fit = curve_fit(piecewise_linear,xvals,yvaleul)
    polyfit =np.poly1d(np.polyfit(xvals, yvaleul, 9))
    #print("polyfitting coefficients")
    #for i in range (20):
    #    print(polyfit[i])
    plt.plot(fit)
    plt.xlim(0,4)
    plt.show()
    plt.plot(xvals,yvaleul)
    plt.plot(xvals,yvalrk2)
    plt.plot(xvals,yvalrk4)
   # plt.plot(xvals,yexact)
    plt.legend(['Euler', 'RK2', 'RK4', 'Exact'], loc='upper left')
    plt.title("Electric field")
    plt.show()

main()
