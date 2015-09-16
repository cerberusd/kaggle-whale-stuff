# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:44:05 2015

@author: minsookim
"""
from glob import glob
from PIL import Image, ImageChops, ImageOps
import numpy as np
import cv2
from matplotlib import pyplot as plt

    #thing=glob('/imgs_subset/w_%d.jpg' % (i))
images=glob('/Users/minsookim/Downloads/kaggle whale/imgs_subset/w_*.jpg' )

R_DIMS=(256,256)

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
        
        
        """
        if i==0:
            new1 = np.asarray(pix_val_flat)
            print len(new1), i
        else:
            new2=np.asarray(pix_val_flat)
            print len(new2), i
            new1=np.vstack((new1,new2))
        """
        
    
    pass

load()
       
       
def resize(image,resize_dims):
    """
    resize an image into a square via padded fit
    using ImageOps.fit for now
    """
    
    resized=ImageOps.fit(image,resize_dims,Image.ANTIALIAS)
    return resized
    
    
def convert():
    """    
    convert json file into cropped images of uniform size 
    """        
    for i in range(500):
        print data[i]['filename'], i
        x=int(data[114]['annotations'][0]['x'])
        y=int(data[114]['annotations'][0]['y'])
        width=int(data[114]['annotations'][0]['width'])
        height=int(data[114]['annotations'][0]['height'])
        cropped=im.crop((x,y,x+width,y+height))
        converted=resize(cropped,R_DIMS)
convert()



    
    

im=Image.open("/Users/minsookim/Downloads/kaggle whale/imgs_subset/w_3.jpg")
#crop(x,y,x+width,y+height)
temp=im.crop((920,1008,1213,1297))