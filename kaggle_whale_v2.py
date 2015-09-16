# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:30:05 2015

@author: minsookim
"""

import json
from pprint import pprint
from glob import glob
from PIL import Image
import pandas
import numpy as np

images=glob('/Users/minsookim/Documents/whale_faces_smerity.json' )
with open('/Users/minsookim/Documents/whale_faces_smerity.json') as data_file:    
    data = json.load(data_file)

pprint(data)

data[0]['annotations'][0]['class']


