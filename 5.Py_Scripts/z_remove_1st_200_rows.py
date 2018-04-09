
# coding: utf-8

# In[99]:


import pandas as pd
import csv


# In[121]:


in1 = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Vipul_Blink.csv")
in2 = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Modify_New_Data/Vipul_Claps.csv")


# In[122]:


in1 = in1.drop(in1.index[0:201])
in1.to_csv("Vipul_Blink_R.csv")


# In[123]:


in2 = in2.drop(in2.index[0:201])
in2.to_csv("Vipul_Claps_R.csv")

