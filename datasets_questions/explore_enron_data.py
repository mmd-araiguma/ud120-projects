#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
"""
print(len(enron_data))
print(len(enron_data["GLISAN JR BEN F"]))
count=0
for i in enron_data:
	if enron_data[i]["poi"]==1:
		print(i)
		count+=1
print(count)
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])
count=0
count2=0
for i in enron_data:
	if enron_data[i]["salary"]!="NaN":
		#print(i)
		count+=1
	if enron_data[i]["email_address"]!="NaN":
		#print(i)
		count2+=1
print(count)
print(count2)
"""
count=0
count2=0
for i in enron_data:
	if enron_data[i]["total_payments"]=="NaN":
		#print(i)
		count+=1
		if enron_data[i]["poi"]==True:
			#print(i)
			count2+=1
print(len(enron_data))
print(count)
print(count2)
print(count2*100.0/count)

import sys
sys.path.append('../tools')
import feature_format as FF
feature_list=["poi", "salary", "bonus"]
data_array=FF.featureFormat(enron_data,feature_list)
features=FF.targetFeatureSplit(data_array)