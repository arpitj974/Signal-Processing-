
# coding: utf-8

# In[33]:


from sklearn.preprocessing import normalize
import csv
import pandas as pd
import numpy as np


# In[50]:


data1=pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Concatenated_Data/archit_ConcatBlink.csv")
data2=pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Concatenated_Data/archit_ConcatClaps.csv")


# In[51]:


data1 = data1.transpose()
a = pd.DataFrame(normalize(data1))
b = a.transpose()
#b.to_csv('arpit_Blink_Norm.csv')


data2 = data2.transpose() 
x = pd.DataFrame(normalize(data2))
y = x.transpose()
b.to_csv('archit_Blink_Norm.csv')
y.to_csv('archit_Claps_Norm.csv')


# In[37]:


"""data2 = data2.transpose() 
x = pd.DataFrame(normalize(data2))
y = x.transpose()
y.to_csv('anil_Claps_Norm.csv')
"""

