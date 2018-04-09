from NeuroPy import NeuroPy
from time import sleep
from time import time
import pandas as pd
import numpy as np
import csv
import pickle
from sklearn.model_selection import train_test_split

neuropy = NeuroPy("/dev/rfcomm1") 
neuropy.start()
sleep(3)


with open('Predict_Final.csv', 'w') as csvfile:
    fieldnames = ['attention', 'delta', 'meditation', 'rawValue', 'theta', 
    'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'midGamma', 'poorSignal', 'blinkStrength' ,'label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    i = time()
    j = time()
    print "Perform the Action"
    sleep(4)
    while(j-i<10):
    	writer.writerow({'attention': neuropy.attention, 'delta': neuropy.delta, 
    		'meditation': neuropy.meditation, 'rawValue': neuropy.rawValue, 
    		'theta': neuropy.theta, 'lowAlpha': neuropy.lowAlpha, 'highAlpha': neuropy.highAlpha, 
    		'lowBeta': neuropy.lowBeta, 'highBeta': neuropy.highBeta, 
    		'lowGamma' : neuropy.lowGamma, 'midGamma' : neuropy.midGamma, 
    		'poorSignal' : neuropy.poorSignal, 'blinkStrength': neuropy.blinkStrength})
        sleep(0.1)
        j = time()
    i = time() 
csvfile.close()
neuropy.stop()

sleep (1)

#print "Read"

input_csv = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Predict_Final.csv")
char1 = dict()
for i in range(1,45) :
    char = {}
    k=0
    for j in range(i-1,i+9) :
        for z in range(1,14) :
            char[k+z-1] = input_csv.iloc[j][z-1]
        k=k+13
    char1[i]=char

#print "Predict"
    
with open('Predict_Concat_Final.csv', 'w') as out_csv:
    column_name = range(0,130)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<45) :
        writer.writerow(char1[j])
        j=j+1

#print "Concatenated"

from sklearn.preprocessing import normalize

data1=pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Predict_Concat_Final.csv")
###### importing the classfier

#print "Normalized"

random_forest_model_pkl = open('Random_Forest_Classifier.pkl', 'rb')
rnd_clf = pickle.load(random_forest_model_pkl)
#print rnd_clf

data1 = data1.drop(data1.index[0:11])
data1 = data1.transpose()
a = pd.DataFrame(normalize(data1))
b = a.transpose()
b.to_csv('Predict_Norm_Final.csv')
data_features = [x for x in b.columns]
data_labels = b.columns[1]
features_train, features_testst, labels_train, labels_test = train_test_split(b[data_features], b[data_labels], test_size=0.05)

predict = rnd_clf.predict(features_train)

sum1 = 0
sum2 = 0

for i in range(0,len(predict)) :
    if predict[i] == 1 :
        sum1 = sum1+1
    else :
        sum2 = sum2+1

#print predict

#print "Blinks = ",sum1," Claps = ",sum2

if sum1>sum2 :
    print "Blink "
else :
    print "Claps"
