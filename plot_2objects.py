# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:56:24 2017

@author: Kafung
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#%matplotlib inline

def plot_2objects(x1, y1, z1, x2, y2, z2) :
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x1, y1, z1, color = 'c') 
    ax.scatter(x2, y2, z2)