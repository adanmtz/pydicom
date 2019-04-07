#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 00:26:13 2019
This script helps you to read and display multiple DICOM files from a folder
and visualize as a film in the same window
@author: Adán Martínez Sixto
"""

#%%Modules to use
from pydicom import read_file
import matplotlib.pyplot as plt
import glob

#%%Data Adquisition
imagenes = []
path = "/folder/where/is/the/dataser*.*"

for file in glob.glob(path):
    imagenes.append(read_file(file).pixel_array)
    
#%%Display Images in one windows as a film

for i in range(len(imagenes)):
    plt.imshow(imagenes[i],cmap=plt.cm.gray)
    plt.pause(1) #delay to view images
