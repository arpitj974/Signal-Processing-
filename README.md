# Signal Processing Of EEG Signals Using Machine Learning

_The aim of this project is to collect the raw electrical signals from a human brain using a neuro headset and then process these signals using machine learning so as to recognise the activity performed by the user._

### Applications:

- This project may serve the purpose of user friendly prosthetic organs directly controlled by brain.
- It may also have application in Automation (Internet of Things) by controlling various devices using signals from brain.

### Requirements:

- Neurosky Mindwave Mobile Headset
- Python 2.7 / jupyter notebook (python 2.7 compatible)

If you have the neuro Headset, go to [With HeadSet](#with-headset), else go to [Without HeadSet](#without-headset)



#### With HeadSet (Implemented in Ubuntu Desktop)

For those who have the neuro headset, they may proceed as following to utilise my project-

1. Switch On the headset and hold the key for On position until the headset flash starts blinking faster, which means it is in pairing mode.

2. Pair your computer with the headset using bluetooth of your computer(The name of the headset for bluetooth connections is Mindwave Mobile).

3. You only have to pair using the bluetooth. To connect the headset, you have to use the following python code in Terminal

``` bash
sudo rfcomm bind /dev/rfcomm1 74:E5:43:D5:6C:07
ls -l /dev/rfcomm1
```

You need to go to your bluetooth settings and then find out the port by which you are connecting to the headset and then replace that port instead of rfcomm1 in the above code(example- rfcomm2,rfcomm3 etc.)

4. You are now connected to the headset.

5. To implement my model, you may use "Final_+project.py" script present in my repository under Py_scripts folder.In this script you have to make a change in the following line of code-
``` bash
input_csv = pd.read_csv("/media/arpit/New Volume/3.Projects/EEG_Project/Raw_Data/Total_Normalised_data_Collection/Predict_Final.csv")
```
Actually the data you collected is written in a csv file in the directory where you have run the above script "Final_+project.py" in a file named **Predict_Final.csv** , so instead of  ` "/media/arpit/New Volume/3.Projects/EEG_Project/Raw_Data/Total_Normalised_data_Collection" ` in above line of code you have to put the address of the directory in which you have run the script "Final_+project.py".

- make sure you change only the path and not the file name that is the file names "Predict_Final.csv" and "Predict_Concat_Final.csv" remains same.

Moreover there is another line of code where you need to change - `"/media/arpit/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Predict_Concat_Final.csv"`. Here also instead of `"/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection"` , put the address of the directory where you have run the script "Final_+project.py".

6. My training dataset is for only two actions - clapping and blinking. So after running the script ,perform one of the above actions and after some time your action will be predicted.

#### Without HeadSet

For those of you who do not have the neuro sky mindwave headset and wish to see the accuracy of my model, proceed as following -

1. Download the file "Final_Normalised_Dataset.csv" from Final Dataset folder in my repository.

2. Now you have to run the python script named "Model_of_3_algos.py" in my repository under the Py_scripts folder.

3. You need to make a small change in the above script before running it.

``` bash
data = pd.read_csv("/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Final_Normalised_DataSet.csv")
```

In the above line of code , you need to change the path from `"/media/joseph/New Volume/3.Projects/ARIES_EEG_Project/Raw_Data/Total_Normalised_data_Collection/Final_Normalised_DataSet.csv"` to the path where you have downloaded the `"Final_Normalised_Dataset.csv"` file.

3. The above script will split the final dataset into two parts, one for testing and another for training.

4. You will get the accuracy score using a module from sklearn.
