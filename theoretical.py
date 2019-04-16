# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:14:31 2019

@author: fsk16
"""

import numpy as np
import pylab as pl

x = np.arange(-1,1,0.009)/5*10**(-3)
y = np.arange(-1, 1,0.009)/5*10**(-3)
k = 2*np.pi / 543e-9
theta = 0.7e-3
omega0 = 106e-6
d = 50e-6
phi = 3.34e-2
R = 0.005 

Matrix_vortex = np.zeros([len(y), len(x)])   
for i in range(len(x)):
    for j in range(len(y)):
        x_ = x[i]
        y_ = y[j]
        if x_ == 0 :
            print("x == 0")
            Matrix_vortex[j,i] = 0
        else:
            Matrix_vortex[j,i] = (4*(k**2)*(theta**2)*np.exp(-2*d**2/omega0**2)*(x_**2+y_**2)* np.exp(-2*(x_**2+y_**2)/(omega0**2)))

Matrix_fork = np.zeros([len(y), len(x)])   
for i in range(len(x)):
    for j in range(len(y)):
        x_ = x[i]
        y_ = y[j]
        if x_ < 0 :
            Matrix_fork[j,i] = (4*(k**2)*(theta**2)*np.exp(-2*d**2/omega0**2)*(x_**2+y_**2) + 1 + k * theta * np.exp(-d*d/omega0/omega0)* (np.sqrt(x_**2+y_**2)) * np.sin(np.arctan(y_/x_) - k*x_*phi))* np.exp(-2*(x_**2+y_**2)/(omega0**2))
        else:  
            Matrix_fork[j,i] =  (4*(k**2)*(theta**2)*np.exp(-2*d**2/omega0**2)*(x_**2+y_**2) + 1 + k * theta * np.exp(-d*d/omega0/omega0)* (np.sqrt(x_**2+y_**2)) *- np.sin(np.arctan(y_/x_) - k*x_*phi))* np.exp(-2*(x_**2+y_**2)/(omega0**2))
        
Matrix_spiral = np.zeros([len(y), len(x)])   
for i in range(len(x)):
    for j in range(len(y)):
        x_ = x[i]
        y_ = y[j]
        if x_ < 0 :
            Matrix_spiral[j,i] = (4*(k**2)*(theta**2)*np.exp(-2*d**2/omega0**2)*(x_**2+y_**2) + 1 + k * theta * np.exp(-d*d/omega0/omega0)* (np.sqrt(x_**2+y_**2)) * np.sin(np.arctan(y_/x_) - k * (x_**2 + y_**2)/(2*R)))* np.exp(-2*(x_**2+y_**2)/(omega0**2))
        else:             
            Matrix_spiral[j,i] = (4*(k**2)*(theta**2)*np.exp(-2*d**2/omega0**2)*(x_**2+y_**2) + 1 + k * theta * np.exp(-d*d/omega0/omega0)* (np.sqrt(x_**2+y_**2)) * - np.sin(np.arctan(y_/x_) - k * (x_**2 + y_**2)/(2*R)))* np.exp(-2*(x_**2+y_**2)/(omega0**2))
        

pl.figure(1)
pl.contourf(x , y, Matrix_spiral , 500)
#pl.axis([-0.0001,0.0001,-0.0001,0.0001])

pl.figure(3)
pl.contourf(x , y, Matrix_fork , 500)

pl.figure(2)
pl.contourf(x , y, Matrix_vortex , 500)
#pl.scatter(x , ((x**2+0.5**2)**0.5)*np.sin(np.arctan(0.5/x)))

#pl.figure(3)
#pl.plot(x , Matrix_fork[100-10])
#pl.axis([-0.00002,0.00002,0,10])
#pl.scatter(x , ((x**2+0.5**2)**0.5)*np.sin(np.arctan(-0.5/x)))
#def fork(x,y):
#    return np.sin(np.arctan(y/x))
#pl.scatter(x , np.sin(np.arctan()))
