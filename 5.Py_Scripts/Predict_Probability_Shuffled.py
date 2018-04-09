
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
get_ipython().magic(u'matplotlib inline')


# In[26]:


data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Final_Normalised_DataSet.csv")
pred_data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Final_Normalised_DataSet.csv")


# In[27]:


labels = 'Label'
features = [x for x in data.columns if x not in labels]
data_labels = data[labels]
data_features = data[features]


# In[28]:


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(data_features, data_labels, test_size=0.33)


# In[29]:


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



# In[35]:


proba_array = clf.predict_proba(features_test)
proba_class_one = proba_array[:,0]
proba_class_two = proba_array[:,1]
print proba_array


# In[34]:


#x = range(0,len(proba_class_one))
#plt.plot(x, proba_class_one)
x= range(0,100)
plt.plot(x, proba_class_one[0:100])


# In[32]:


x = range(0,len(proba_class_two))
plt.plot(x, proba_class_two)
#x = range(0,100)
#plt.plot(x, proba_class_two[0:100])


# In[21]:


from sklearn.svm import SVC
clf=SVC(probability = True)

features_train = features_train[0:len(features_train)]
features_test = features_test[0:len(features_test)]

labels_train = labels_train[0:len(labels_train)]
labels_test = labels_test[0:len(labels_test)]

clf.fit(features_train,labels_train)

prediction_svm=clf.predict(features_train)
accur = accuracy_score(prediction_svm, labels_train)
print "SVM Training Accuracy = ",accur

prediction_svm = clf.predict(features_test)
accur = accuracy_score(prediction_svm, labels_test)
print "SVM Testing accuracy = ",accur

cnf_matrix_svm = confusion_matrix(labels_test, prediction_svm)
print "Testing Con Matrix SVM \n",cnf_matrix_svm


# In[22]:


proba_array = clf.predict_proba(features_test)
proba_class_one = proba_array[:,0]
proba_class_two = proba_array[:,1]


# In[23]:


x = range(0,len(proba_class_one))
plt.plot(x, proba_class_one)
#x= range(0,100)
#plt.plot(x, proba_class_one[0:100])


# In[24]:


x = range(0,len(proba_class_two))
plt.plot(x, proba_class_two)
#x = range(0,100)
#plt.plot(x, proba_class_two[0:100])

