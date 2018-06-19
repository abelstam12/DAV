import os
import pandas as pd
import numpy as np

def get_data_path(filename):
    current_path = os.getcwd().split('/')
    return '/'.join(current_path[0:-1]) + '/Data' + '/' + filename

def get_pandas(filename, encoding='LATIN-1', sep = ';'):
    return pd.read_csv(get_data_path(filename), encoding = encoding, sep = sep)

def get_deliverables_path():
    current_path = os.getcwd().split('/')
    return '/'.join(current_path[0:-1]) + '/deliverables' + '/'

def get_clean_data(data):
    '''
    Takes list with strings as argument and tries to get the numeric value of
    the string. If there is no numerical representation, disregard entry.
    Note this can only be used to obtain clean numerical data.
    '''
    float_array = np.zeros(len(data))
    index = 0
    for element in data:
        if (type(element) == str):
            # if its a string
            fl = element.replace(',', '.')
        try:
            fl = float(fl)
        except:
            # here the string cannot be formatted to a float so the entrie is ignored
            float_array = float_array[:len(float_array) -2]
            continue
        float_array[index] = fl
        index += 1
    return float_array
        