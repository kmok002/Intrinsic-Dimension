# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:22:10 2017

@author: Kafung
"""
import matplotlib as mpl 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#%matplotlib inline

#Inputs xs, ys, zs, representing the x,y,and z coordinates of the points respectively and plots them. 
def plot_1object(xs, ys, zs) : 
    
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d')
    
    return ax.scatter(xs,ys,zs)
    