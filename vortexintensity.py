# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:40:41 2019

@author: fsk16
"""

import numpy as np
import pylab as pl
import time
#from mpl_toolkits import mplot3d

def y_at_x(x):
    y_at_x = np.zeros([height,1])
    for row in range(Matrix.shape[0]):
        y_at_x[row] = Matrix[row][x]
    return y_at_x

height = 1088           # Needs to be set for each file
width = 2048            # Needs to be set, given in info lines
pixel = 5.5e-3

x = 0                   # column index of the matrix set to zero
y = 0                   # row index of the matrix set to zero

before = time.time()
with open("3z=50exp60.txt") as f:
    lines = f.readlines()           # Each line is y = y'
    info = lines[0:8]
    Matrix = np.zeros([height,width])  
    print(info)                     # Read what height and width is, and pixel size
    for i in lines[8:len(lines)-1]:
        a = ''                              # Data is in string, initialize each data a
        for j in i:
            a = a + j                       # Update reading
            if j == ';':                    # Data seperation reached
                a = a[:len(a)-1]            # Subtract ;
                Matrix[y,x] = float(a)      # Add data as a float
                x = x + 1                   # Going along the row
                a = ''
        y = y + 1                           # Next row
        x = 0                               # Back to the first column
after = time.time()
# FIGURE
print("time to read doc is ", after-before)
x = np.arange(0,width,1) *pixel                  # x distance, multiply with physical length of a pixel
y = np.arange(0,height,1)  *pixel       # y distance, multiply with physical length of a pixel

Y = 2.2
X = 5.7

Y_pixel = int(Y *height /(height*pixel))
X_pixel = int(X *width /(width*pixel))

before = time.time()

pl.figure(2 , figsize = (5,5))
pl.contourf(x, y, Matrix, 100)
pl.axis([X-1.5,X+1.5,Y-1.5,Y+1.5])
pl.xlabel("x (mm)")
pl.ylabel("y (mm)")

after = time.time()

print("time to plot 2D is ", after - before)
#
#pl.figure(1 , figsize = (7,5))
#
#pl.plot(x , Matrix[Y_pixel])
#pl.axis([X-1.5,X+1.5,0,1000])
#pl.xlabel("x (mm)")
#pl.ylabel("Intensity")
#
#pl.figure(3 , figsize = (7,5))
#
#pl.plot(y , y_at_x(X_pixel))
#pl.axis([Y-1.5,Y+1.5,0,1000])
#pl.xlabel("y (mm)")
#pl.ylabel("Intensity")

""" SECOND VORTEX """ 

x = 0                   # column index of the matrix set to zero
y = 0                   # row index of the matrix set to zero

before = time.time()
#with open("2z=10.txt") as f:
#    lines = f.readlines()           # Each line is y = y'
#    info = lines[0:8]
#    Matrix = np.zeros([height,width])  
#    print(info)                     # Read what height and width is, and pixel size
#    for i in lines[8:len(lines)-1]:
#        a = ''                              # Data is in string, initialize each data a
#        for j in i:
#            a = a + j                       # Update reading
#            if j == ';':                    # Data seperation reached
#                a = a[:len(a)-1]            # Subtract ;
#                Matrix[y,x] = float(a)      # Add data as a float
#                x = x + 1                   # Going along the row
#                a = ''
#        y = y + 1                           # Next row
#        x = 0                               # Back to the first column
after = time.time()
# FIGURE
print("time to read doc is ", after-before)
x = np.arange(0,width,1) *pixel                  # x distance, multiply with physical length of a pixel
y = np.arange(0,height,1)  *pixel       # y distance, multiply with physical length of a pixel

Y = 3.15
X = 4.95

Y_pixel = int(Y *height /(height*pixel))
X_pixel = int(X *width /(width*pixel))

before = time.time()

#pl.figure(1 , figsize = (5,5))
#pl.contourf(x, y, Matrix, 100)
#pl.axis([X-1.5,X+1.5,Y-1.5,Y+1.5])
#pl.xlabel("x (mm)")
#pl.ylabel("y (mm)")

after = time.time()

print("time to plot 2D is ", after - before)

#pl.figure(1 , figsize = (7,5))
#
#pl.plot(x , Matrix[Y_pixel])
#pl.axis([X-1.5,X+3,0,1100])
#pl.xlabel("x (mm)")
#pl.ylabel("Intensity")
#pl.legend(["d = 85um, y = 3.15mm" , "d = 50um, y = 2.20mm"])
#
#
#pl.figure(3 , figsize = (7,5))
#
#pl.plot(y , y_at_x(X_pixel))
#pl.axis([Y-1.5,Y+3,0,1000])
#pl.xlabel("y (mm)")
#pl.ylabel("Intensity")
#pl.legend(["d = 85um, x = 6.35mm" , "d = 50um, x = 4.90mm"])


""" THIRD VORTEX """ 

x = 0                   # column index of the matrix set to zero
y = 0                   # row index of the matrix set to zero

before = time.time()
#with open("3z=10exp60.txt") as f:
#    lines = f.readlines()           # Each line is y = y'
#    info = lines[0:8]
#    Matrix = np.zeros([height,width])  
#    print(info)                     # Read what height and width is, and pixel size
#    for i in lines[8:len(lines)-1]:
#        a = ''                              # Data is in string, initialize each data a
#        for j in i:
#            a = a + j                       # Update reading
#            if j == ';':                    # Data seperation reached
#                a = a[:len(a)-1]            # Subtract ;
#                Matrix[y,x] = float(a)      # Add data as a float
#                x = x + 1                   # Going along the row
#                a = ''
#        y = y + 1                           # Next row
#        x = 0                               # Back to the first column
after = time.time()
# FIGURE
print("time to read doc is ", after-before)
x = np.arange(0,width,1) *pixel                  # x distance, multiply with physical length of a pixel
y = np.arange(0,height,1)  *pixel       # y distance, multiply with physical length of a pixel

Y = 1.7
X = 6.2

Y_pixel = int(Y *height /(height*pixel))
X_pixel = int(X *width /(width*pixel))

before = time.time()

#pl.figure(3 , figsize = (5,5))
#pl.contourf(x, y, Matrix, 100)
#pl.axis([X-2.5,X+2.5,Y-2.5,Y+2.5])
#pl.xlabel("x (mm)")
#pl.ylabel("y (mm)")

after = time.time()

print("time to plot 2D is ", after - before)

#pl.figure(1 , figsize = (7,5))
#
#pl.plot(x , Matrix[Y_pixel])
#pl.axis([X-3,X+2,0,3000])
#pl.xlabel("x (mm)")
#pl.ylabel("Intensity")
#pl.legend(["d = 85um, y = 4.41mm" , "d = 50um, y = 3.15mm", "d =150um, y = 1.70mm"])
#
#
#pl.figure(3 , figsize = (7,5))
#
#pl.plot(y , y_at_x(X_pixel))
#pl.axis([Y-1.5,Y+4,0,3000])
#pl.xlabel("y (mm)")
#pl.ylabel("Intensity")
#pl.legend(["d = 85um, x = 6.17mm" , "d = 50um, x = 4.95mm", "d =150um, x = 6.20mm"])




