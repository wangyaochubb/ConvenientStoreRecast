# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:19:29 2016

@author: u041018
"""

# try to read in fix-width text file
#%%
import pandas as pd
#%%
width = [3,4,8,6,18,3,3,30,3,15,12,2,8,8,8,1]
origtextfile =  "H:/7-Eleven/test/off.txt"
df = pd.read_fwf(origtextfile,header=None,widths = width, index_col = 0)