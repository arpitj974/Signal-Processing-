
# coding: utf-8

# In[2]:


import csv
import pandas as pd
import numpy as np


# In[5]:


######## blink data Label = 1
input_csv=pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Anil_Blink_R.csv")
char1 = dict()
for i in range(1,691) :
    char = {}
    #char[0]='1'
    k=0
    for j in range(i-1,i+9) :
        for z in range(1,14) :
            char[k+z-1] = input_csv.iloc[j][z-1]
        k=k+13
    char1[i]=char
    
with open('anil_ConcatBlink.csv', 'w') as out_csv:
    column_name = range(0,130)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<691) :
        writer.writerow(char1[j])
        j=j+1


# In[6]:


######## claps data Label = 2
input_csv2=pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Anil_Claps_R.csv")
char2 = dict()
for i in range(1,691) :
    charc = {}
    #charc[0]='2'
    k=0
    for j in range(i-1,i+9) :
        for z in range(1,14) :
            charc[k+z-1] = input_csv2.iloc[j][z-1]
        k=k+13
    char2[i]=charc
    
with open('anil_ConcatClaps.csv', 'w') as out_csv:
    column_name = range(0,130)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<691) :
        writer.writerow(char2[j])
        j=j+1


# In[10]:


"""with open('varun_ModifyBlink.csv', 'w') as out_csv:
    column_name = range(0,131)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<691) :
        writer.writerow(char1[j])
        j=j+1
    """


# In[11]:


"""with open('varun_ModifyClaps.csv', 'w') as out_csv:
    column_name = range(0,131)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<691) :
        writer.writerow(char2[j])
        j=j+1
        
    """

