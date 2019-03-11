# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:41:32 2019

@author: fsk16
"""

import numpy as np
import pylab as pl

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)



def matrix(x , y):
    two_dim_matrix = np.zeros([len(y) , len(x)])
    for i in range(len(x)):
        for j in range(len(y)):
            if np.arctan(y[j]/x[i]) >= 0:
                two_dim_matrix[j][i] =  np.arctan(y[j]/x[i]) - np.pi/2
            else:
                two_dim_matrix[j][i] =  np.arctan(y[j]/x[i]) + np.pi/2
    return two_dim_matrix

pl.figure(1)
pl.contourf(x , y , matrix(x,y) , 100)

pl.figure(2)
pl.plot(x,np.arctan(x)-np.pi/2,'r')
pl.plot(x,np.arctan(x)+np.pi/2)