import numpy as py
import math as mth
from ODEtest import *
import matplotlib.pyplot as plt
from scipy import optimize
#stepsize0.5 to start
def main():
    height = 10.0
    #ode = ODErealefield(height)
    #nsteps = int( input( "Enter number of steps ") )
    delta = float (input( "Enter step size "))
    nsteps = int(4.0/delta)
    initvali = [0.,0.]
    initvalii= [0.,0.]
    #printcheck
    print ("Running with  nsteps = %d and dx = %s" % ( nsteps,delta))
    def ro(x):
        if x<1:
            return 0.
        if 1<=x<=2:
            return float(height)
        if 2<x<=3:
            return float((-1.0)*height)
        if 3<=x<=4.05:
            return 0.
        
   # print(ro(2))
        
    def gradientEUL(x,yinit,step):
        ynew = yinit + step*ro(x)
        return(ynew)
    def gradrk4(x,yinit,step):
        d1 = ro(x)
        d2 = ro(x+step/2) 
        d3 = ro(x+step/2)
        d4 = ro(x+step)
        ynew = yinit +  (step)*(1.0/6.0)*(d1 + 2*(d2) + 2*(d3) + (d4))
        return float(ynew)
    
    xvals =[]
    xvals.append(initvali[0])
    yevals=[]
    yvvals=[]
    #EULER
    yevals.append(initvali[1])
    yvvals.append(initvali[1])
    #print(yevals)
    #print(yvvals)
    val=0
    for i in range(nsteps):
        #print (i)
        val += delta
        #print (val)
        xvals.append(val)
        if i<=1:
            y = gradientEUL(val,yevals[0],delta)
           # print("y=")
           # print(y)
            yevals.append(y)
            vinit = 0
            yvvals.append(vinit)
        else:
           # print("p=")
            p = gradientEUL(val,yevals[i-1],delta)
            #can use the same idea here and do a euler plot for v straight away
            v = yvvals[i-1] + delta*((-1.0)*yevals[i])
            yvvals.append(v)
           # print(p)
            yevals.append(p)
   # print (yvvals)
   # print (yevals)
   


    
   # xnewvals =[]
   # xnewvals.append(initvali[0])
    ynewevals=[]
    ynewvvals=[]
    ynewevals.append(initvali[1])
    ynewvvals.append(initvali[1])
    #now for runge kutta
    #makes sure that we are using the right value of x for calculating y
    val=0
    #calculating e fields with runge kutta 4
    for i in range(nsteps):
        if i<1:
            val+=delta
            y = gradrk4(val,ynewevals[0],delta)
            ynewevals.append(y)
        else:
            val+=delta
            p = gradrk4(val,ynewevals[i-1],delta)
            ynewevals.append(p)
        

    



    val=0
    for i in range(nsteps):
        val += delta
    #    xnewvals.append(val)
        if i<1:
           # y = gradrk4(val,ynewevals[0],delta)
           # ynewevals.append(y)
            vnewinit = 0
            ynewvvals.append(vnewinit)
            print("done here")
        elif i==(nsteps-2): #allowed i+1
           # p = gradrk4(val,ynewevals[i-1],delta)
            #can use the same idea here and do a euler plot for v straight away
            v = ynewvvals[i-1] + delta*(1.0/3.0)*((-1.0)*(ynewevals[i] + 2*(ynewevals[i+1])))
            ynewvvals.append(v)
           # ynewevals.append(p)
        elif i==(nsteps-1): #allow i
           # p = gradrk4(val,ynewevals[i-1],delta)
            #can use the same idea here and do a euler plot for v straight away
            v = ynewvvals[i-1] + delta*((-1.0)*(ynewevals[i]))
            ynewvvals.append(v)
           # ynewevals.append(p)
        elif i==(nsteps-3):#allowed i + 2 values
           # p = gradrk4(val,ynewevals[i-1],delta)
            #can use the same idea here and do a euler plot for v straight away
            v = ynewvvals[i-1] + delta*(-1.0/5.0)*(ynewevals[i] + 2*(ynewevals[i+1]) + 2*(ynewevals[i+2]))
            ynewvvals.append(v)
           # ynewevals.append(p)
        else:
           # p = gradrk4(val,ynewevals[i-1],delta)
           # print(i)
           # print(nsteps)
            v = ynewvvals[i-1] + delta*(1.0/6.0)*((-1.0)*(ynewevals[i] + 2*(ynewevals[i+1]) + 2*(ynewevals[i+2]) + ynewevals[i+3]))
            ynewvvals.append(v)
           # ynewevals.append(p)

   
    
   # plt.figure(1)
    
   # plt.subplot(2,2,1)
    plt.plot(xvals,yevals)
    plt.plot(xvals,yvvals)
    plt.legend(['Electric Field','Potential'])
    plt.title("Euler")
    plt.show()
    
   # plt.subplot(2,2,2)
    plt.plot(xvals,ynewevals)
    plt.plot(xvals,ynewvvals)
    plt.legend(['Electric field','Potential'])
    plt.title("RK4")
    plt.show()



   # plt.plot(xvals,yvaleul)
   # plt.plot(xvals,yvalrk2)
   # plt.plot(xvals,yvalrk4)
   # plt.plot(xvals,yexact)
   # plt.legend(['Euler', 'RK2', 'RK4', 'Exact'], loc='upper left')
   # plt.title("Electric field")
   # plt.show()
    
    #here are plotting a piecewise sinusoidal fit of the first integration (efield)
   # plt.xlim(0,4)
   # plt.plot(xvals,yvaleul)
   # plt.plot(xd, piecewise(xd, *l))
   # plt.legend(['Euler data ', 'Sinusoidal plot for for next integration'], loc='upper left')
   # plt.show()



    
main()
