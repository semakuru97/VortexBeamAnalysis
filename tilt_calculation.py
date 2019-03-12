# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:38:06 2019

@author: fsk16
"""



import numpy as np
import scipy.constants as sc
#Era = 4.87 *10**6 * sc.e
#hra = 1.37e-11
#hrn = 3.79e-3
#
#Ern = (4*84/(np.log(hra/hrn)+4*88/np.sqrt(Era)))**2
#
#print(Ern/sc.e / 10**6)
#print(70e-6/(0.3 * 1.5 * 0.81**2 /8 /5))
#
T = 3e-3 # Width of plate
angle = np.arange(0,20,1) *np.pi/ 180 # Angles from 0 to 10 deg in radians

def displacement(angle, t, n):
    return t *np.sin(angle)*(1-np.cos(angle)/np.sqrt(n*n - np.sin(angle)**2))
def approx_displacement(angle, t, n):
    return t*angle*(1-1/n)

for i in angle:
    print("at angle ", i*180/ np.pi, ", d is: ", displacement(i , T , 1.5)*10**6, "um")
    print("at angle ", i*180/ np.pi, ", approx: ", approx_displacement(i , T , 1.5)*10**6, "um")