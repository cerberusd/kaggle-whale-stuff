# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:44:05 2015

@author: minsookim
"""
from glob import glob
from PIL import Image
import pandas
import numpy as np
    #thing=glob('/imgs_subset/w_%d.jpg' % (i))
images=glob('/Users/minsookim/Downloads/kaggle whale/imgs_subset/w_*.jpg' )

print images

 
def load(subset=True,test=False):
    """
    load function to load all the images in a folder(full or subset) and read in the target values as well
    returns X and y    
    """
    for i in range(len(images)):
        im = Image.open(images[i],'r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        
        if i==0:
            new1 = np.asarray(pix_val_flat)
            print len(new1), i
        else:
            new2=np.asarray(pix_val_flat)
            print len(new2), i
            new1=np.vstack((new1,new2))
        
        
    
    return new3

hi=load()
        
        

