#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
#reading the data in a csv file
confidence_criteria = 0.75
print()


db_training = []
db_Test = []
X = []
Y = []

with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db_Test.append (row)
#print (db_Test)

with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db_training.append (row)
#print (db_training)

Outlook = {
              "Sunny": 1,
              "Overcast": 2,
              "Rain": 3
          }
Temperature = {
                "Cool": 1,
                "Mild": 2,
                "Hot": 3
              }
Humidity = {
              "Normal":1,
              "High":2
          }
Wind = {
          "Weak":1,
          "Strong":2
      }
Class_labels = {
                  "Yes":1,
                  "No":2
              }
#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
for instance in db_training:
  #print(instance[1], instance[2], instance[3], instance[4])
  X.append([Outlook [instance[1]], Temperature[instance[2]], Humidity[instance[3]], Wind[instance[4]] ])
#print(X)
#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for instance in db_training:
 Y.append(Class_labels[instance[5]])
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#convert test data to integer values
#--> add your Python code here
test_set = []

for instance in db_Test:
    test_set.append([Outlook [instance[1]], Temperature[instance[2]], Humidity[instance[3]], Wind[instance[4]] ])
   
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))
print ( "------------------------------------------------------------------------------------------------------")
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for i in range (len(test_set)):
  confidence =  max(clf.predict_proba([test_set[i]])[0])
  max_index = list(clf.predict_proba([test_set[i]])[0]).index(confidence)

  if confidence >= confidence_criteria:
    class_result = "Yes" if max_index == 0 else "No"
    print (str(db_Test[i][0]).ljust(15) + str(db_Test[i][1]).ljust(15) + str(db_Test[i][2]).ljust(15) + str(db_Test[i][3]).ljust(15) +
            str(db_Test[i][4]).ljust(15) + str(class_result).ljust(15) + str(round(confidence,2)).ljust(15) )