import numpy as py
import math as mth
from ODE import *
import matplotlib.pyplot as plt

def main():
    poly = ODEPoly([1.0,2.0,3.0,4.0])
    print(poly.firstderiv([1.0,1.0]))
    
    expon = ODEExp(5.0)
    print(expon.firstderiv([10.0,10.0]))

main()
