
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
get_ipython().magic(u'matplotlib inline')


# In[2]:


data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Final_Normalised_DataSet.csv")


# In[3]:


labels = 'Label'
features = [x for x in data.columns if x not in labels]


# In[4]:


data_labels = data[labels]
data_features = data[features]


# In[5]:


from sklearn.model_selection import train_test_split
features_train, features_testst, labels_train, labels_test = train_test_split(data_features, data_labels, test_size=0.33)


# In[6]:


from sklearn.svm import SVC
clf=SVC(kernel = 'linear')
clf.fit(features_train,labels_train)

prediction_svm=clf.predict(features_train)
accur = accuracy_score(prediction_svm, labels_train)
print "SVM Training Accuracy = ",accur

prediction_svm = clf.predict(features_test)
accur = accuracy_score(prediction_svm, labels_test)
print "SVM Testing accuracy = ",accur

cnf_matrix_svm = confusion_matrix(labels_test, prediction_svm)
print "Testing Con Matrix SVM \n",cnf_matrix_svm


# In[6]:


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)

prediction_dt=clf.predict(features_train)
accur=accuracy_score(prediction_dt, labels_train)
print "DT Training accuracy = ",accur


prediction_dt=clf.predict(features_test)
accur=accuracy_score(prediction_dt, labels_test)
print "DT Testing accuracy =  ",accur


cnf_matrix_dt = confusion_matrix(labels_test, prediction_dt)
print "Testing Con Matri DT \n",cnf_matrix_dt



# In[9]:


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state = 0)
clf.fit(features_train,labels_train)

prediction_rf=clf.predict(features_train)
accur=accuracy_score(prediction_rf, labels_train)
print "RF Training accuracy = ",accur


prediction_rf=clf.predict(features_test)
accur=accuracy_score(prediction_rf, labels_test)
print "RF Testing accuracy =  ",accur


cnf_matrix_rf = confusion_matrix(labels_test, prediction_rf)
print "Testing Con Matri RF \n",cnf_matrix_rf

