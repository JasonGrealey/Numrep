import numpy as py
import math as mth
from ODE import *
import matplotlib.pyplot as plt

def main():
    
    
    types = (input( "Enter function type (exp, sin, poly) "))
    nsteps = int( input( "Enter number of steps ") )
    delta = float( input( "Enter step size "))

    #printcheck
    print ("Running with = %s , nsteps = %d and dx = %d" % ( types, nsteps, delta))
    #Create ODE
    if( types == 'poly' ):
        ode = ODEPoly([ 1.0, 1.0, -3.0, 1.0 ] )
        print(ode.ival)
    elif( types == 'exp' ):
        ode = ODEExp(1.0 )
        print(ode.ival)
    elif( types == 'sin' ):
        ode = ODESinusoid( 1.0 )
        print(ode.ival)
    else:
        print (" No functional form specified: %s" % (types))
        quit()
    
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
    
    yexact = [ode.exactsoln(coords[0]) for coords in eulerres.retall()]
 #   plt.plot(x, x)
  #  plt.plot(x, 2 * x)
   # plt.plot(x, 3 * x)
    #plt.plot(x, 4 * x)


    plt.plot(xvals,yvaleul)
    plt.plot(xvals,yvalrk2)
    plt.plot(xvals,yvalrk4)
    plt.plot(xvals,yexact)
    plt.legend(['Euler', 'RK2', 'RK4', 'Exact'], loc='upper left')
    plt.show()

main()
