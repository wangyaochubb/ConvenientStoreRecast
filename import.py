# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:45:01 2016

@author: Wang Yao
The purpose of this script is to readin and orgnize the raw dataset from 7-Eleven
"""
"""
#The original data file contains some non-standard characters. 
#%%
rawdatafile1 = 'H:/7-Eleven/test/e021995d_OT_013116'
rawdatafile2 = 'H:/7-Eleven/test/e021995t_OT_013116'
#%%
e021995d_OT_013116 = open(rawdatafile1,"r",encoding="utf-8",errors="ignore")
e021995d_OT_31JAN2016 = open("H:/7-Eleven/test/e021995d_OT_31JAN2016.txt","a")
for line in e021995d_OT_013116:
    e021995d_OT_31JAN2016.write(line)
e021995d_OT_013116.close
e021995d_OT_31JAN2016.close
#%%
e021995t_OT_013116 = open(rawdatafile2,"r",encoding="utf-8",errors="ignore")
e021995t_OT_31JAN2016 = open ("H:/7-Eleven/test/e021995t_OT_31JAN2016.txt","a")
for line in e021995t_OT_013116:
    e021995t_OT_31JAN2016.write(line)
e021995t_OT_013116.close
e021995t_OT_31JAN2016.close
#End of converting files
"""
#%%
path = 'H:/7-Eleven/test/'
rawdata = open(path+'e021995d_OT_31JAN2016.txt','r')
#%%
i=0
rawdata.seek(0)
nextline  = rawdata.readline()
#while nextline != ""
while i <= 5:
    if nextline[0:3] == "CLM":
        print('claim')
    elif nextline[0:3] == "NOT":
        print('notes')
    else:
        print('other records')
    nextline = rawdata.readline()
    i += 1
#%%
rawdata.close()
