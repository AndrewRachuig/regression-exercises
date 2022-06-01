import pandas as pd
import numpy as np
# scaler
from sklearn.preprocessing import MinMaxScaler
# train test split from sklearn
from sklearn.model_selection import train_test_split

def split_zillow(df):
    '''
    Takes in a prepped zillow dataframe, splits it into train, validate and test subgroups and then returns those subgroups.
    
    Arguments: df - a cleaned pandas dataframe with the expected feature names and columns in the zillow dataset
    Return: train, validate, test - dataframes ready for the exploration and model phases.
    '''
    train, test = train_test_split(df, train_size = 0.8, random_state = 1234)
    train, validate = train_test_split(train, train_size = 0.7, random_state = 1234)
    return train, validate, test

def data_scaler(train, validate, test):
    '''
    This function takes in train, validate, test subsets of the cleaned zillow dataset and using the train subset creates a min_max 
    scaler. It thens scales the subsets and returns the train, validate, test subsets as scaled versions of the initial data.

    Arguments: train, validate, test - split subsets from of the cleaned zillow dataframe
    Return: scaled_train, scaled_validate, scaled_test - scaled versions of the initial unscaled dataframes
    '''
    
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(train)
    validate_scaled = scaler.transform(validate)
    test_scaled = scaler.transform(test)

    return train_scaled, validate_scaled, test_scaled