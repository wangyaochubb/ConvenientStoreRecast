# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:45:01 2016

@author: U041018
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
# do NOT repeat this procedure, it takes long time
# for loop may be faster
rawdata.seek(0)
nextline  = rawdata.readline()
while nextline != "":
    if nextline[0:3] == "CLM":
        with open(path+"/clm.txt","a") as clm:
            clm.write(nextline)
    elif nextline[0:3] == "NOT":
        with open(path+"/not.txt","a") as note:
            note.write(nextline)
    elif nextline[0:3] == "TOT":
        with open(path+"/tot.txt","a") as tot:
            tot.write(nextline)    
    elif nextline[0:3] == "WD1":
        with open(path+"/wd1.txt","a") as wd1:
            wd1.write(nextline)    
    elif nextline[0:3] == "WD3":
        with open(path+"/wd3.txt","a") as wd3:
            wd3.write(nextline)    
    elif nextline[0:3] == "LD1":
        with open(path+"/ld1.txt","a") as ld1:
            ld1.write(nextline)    
    elif nextline[0:3] == "LD2":
        with open(path+"/ld2.txt","a") as ld2:
            ld2.write(nextline)    
    elif nextline[0:3] == "DD1":
        with open(path+"/dd1.txt","a") as dd1:
            dd1.write(nextline)    
    elif nextline[0:3] == "CTL":
        with open(path+"/ctl.txt","a") as ctl:
            ctl.write(nextline)    
    elif nextline[0:3] == "ADR":
        with open(path+"/adr.txt","a") as adr:
            adr.write(nextline)    
    elif nextline[0:3] == "AGR":
        with open(path+"/agr.txt","a") as agr:
            agr.write(nextline)    
    elif nextline[0:3] == "ACN":
        with open(path+"/acn.txt","a") as acn:
            acn.write(nextline)    
    elif nextline[0:3] == "CST":
        with open(path+"/cst.txt","a") as cst:
            cst.write(nextline)    
    elif nextline[0:3] == "MCF":
        with open(path+"/mcf.txt","a") as mcf:
            mcf.write(nextline)    
    elif nextline[0:3] == "DES":
        with open(path+"/des.txt","a") as des:
            des.write(nextline)
    elif nextline[0:3] == "ICD":
        with open(path+"/icd.txt","a") as icd:
            icd.write(nextline)
    elif nextline[0:3] == "LEG":
        with open(path+"/leg.txt","a") as leg:
            leg.write(nextline)    
    elif nextline[0:3] == "NET":
        with open(path+"/net.txt","a") as net:
            net.write(nextline)    
    elif nextline[0:3] == "OFF":
        with open(path+"/off.txt","a") as off:
            off.write(nextline)    
    elif nextline[0:3] == "PAY":
        with open(path+"/pay.txt","a") as pay:
            pay.write(nextline)    
    elif nextline[0:3] == "PRC":
        with open(path+"/prc.txt","a") as prc:
            prc.write(nextline)    
    elif nextline[0:3] == "ACR":
        with open(path+"/acr.txt","a") as acr:
            acr.write(nextline)    
    elif nextline[0:3] == "REC":
        with open(path+"/rec.txt","a") as rec:
            rec.write(nextline)    
    elif nextline[0:3] == "RED":
        with open(path+"/red.txt","a") as red:
            red.write(nextline)    
    elif nextline[0:3] == "REI":
        with open(path+"/rei.txt","a") as rei:
            rei.write(nextline)    
    elif nextline[0:3] == "RES":
        with open(path+"/res.txt","a") as res:
            res.write(nextline)    
    elif nextline[0:3] == "RST":
        with open(path+"/rst.txt","a") as rst:
            rst.write(nextline)    
    elif nextline[0:3] == "SSN":
        with open(path+"/ssn.txt","a") as ssn:
            ssn.write(nextline)    
    elif nextline[0:3] == "WRK":
        with open(path+"/wrk.txt","a") as wrk:
            wrk.write(nextline)    
    else:
        with open(path+"/other.txt","a") as other:
            other.write(nextline)
    nextline = rawdata.readline()
#%%
rawdata.close()
