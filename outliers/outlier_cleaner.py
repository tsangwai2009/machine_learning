#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    ### your code goes here
    uncleaned_data=[]
    error=[]
    for i in range(0,len(predictions)):
        tup=()
        tup=(ages[i][0],net_worths[i][0],net_worths[i][0]-predictions[i][0])
        uncleaned_data.append(tup)


    for j in range(0,len(uncleaned_data)):
        cleaned_data = sorted(uncleaned_data, key = lambda x: abs(x[2]))
        cleaned_data = cleaned_data[0:int(len(uncleaned_data)*0.9)]
    print(len(cleaned_data))
    return cleaned_data

