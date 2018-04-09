
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
get_ipython().magic(u'matplotlib inline')


# In[2]:


data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/predi_proba_unshuffled_train.csv")
pred_data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/predi_proba_unshuffled.csv")


# In[3]:


f = data.columns
z = list()
for i in range(1,130) :
    #print f[i]
    if int(f[i])%13==12 :
        z.append(f[i])


# In[4]:


labels = 'Label'
#features = [x for x in data.columns if x not in labels and x not in z]
features = [x for x in data.columns if x not in labels]
data_labels = data[labels]
data_features = data[features]


# In[5]:


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(data_features, data_labels, test_size=0.33)


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


# In[7]:


clf.feature_importances_


# In[9]:


predict = clf.predict(pred_data[features])
accura = accuracy_score(predict ,pred_data[labels])
print accura

cnf_matrix_dt = confusion_matrix(pred_data[labels], predict)
print "Testing Con Matri DT \n",cnf_matrix_dt


# In[102]:


pred_data_features = pred_data[features]


# In[103]:


proba_array = clf.predict_proba(pred_data_features)
proba_class_one = proba_array[:,0]
#proba_class_two = proba_array[:,1]
print proba_array


# In[104]:


#x = range(0,len(proba_class_one))
#plt.plot(x, proba_class_one)
x= range(0,2071)
plt.plot(x, proba_class_one[0:2071])


# In[21]:


pred_data.iloc[2001][0]


# In[22]:


#x = range(0,len(proba_class_two))
#plt.plot(x, proba_class_two)
x = range(2072,len(proba_class_one))
plt.plot(x, proba_class_one[2072:])


# In[29]:


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


# In[55]:


x = pred_data.iloc[1001][1:]
x1 = pred_data.iloc[2][1:]
y = pred_data.iloc[1001][0]
y1 = pred_data.iloc[2][0]
print clf.predict([x,x1])
y


# In[31]:


prediction_rf=clf.predict(pred_data[features])
accur=accuracy_score(prediction_rf, pred_data[labels])
print "RF Testing accuracy =  ",accur


cnf_matrix_rf = confusion_matrix(pred_data[labels], prediction_rf)
print "Testing Con Matri RF \n",cnf_matrix_rf

