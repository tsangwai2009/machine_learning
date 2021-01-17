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

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))

#print([list(enron_data)[i] for i in range(0,len(enron_data))])
print([list(enron_data.values())[i]['poi'] for i in range(0,len(enron_data))].count(True))
#print(enron_data["PRENTICE JAMES"]['total_stock_value'])
#print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
#print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])
#print([list(enron_data.keys())])
#print([list(list(enron_data.values())[0].keys())])

#LAY KENNETH L SKILLING JEFFREY K FASTOW ANDREW S
#print(len(enron_data))
#print([list(enron_data.values())[i]['total_payments'] for i in range(0,len(enron_data))].count('NaN'))

for i in range(0,len(enron_data)):
    if list(enron_data.values())[i]['poi']==True :
        print([list(enron_data.values())[i]['total_payments']])
    

