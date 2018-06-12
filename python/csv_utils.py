import os
import pandas as pd
import numpy as np

def get_data_path(filename):
    current_path = os.getcwd().split('/')
    return '/'.join(current_path[0:-1]) + '/Data' + '/' + filename

def get_pandas(filename, encoding='LATIN-1', sep = ';'):
    return pd.read_csv(get_data_path(filename), encoding = encoding, sep = sep)

def get_float(data):
    '''
    Takes list with strings as argument and tries to get the numeric value of
    the string.
    '''
    float_array = np.zeros(len(data))
    index = 0
    for element in data:
        fl = element.replace(',', '.')
        try:
            fl = float(fl)
        except:
            # here the string cannot be formatted to a float
            fl = ''
        float_array[index] = fl
        index += 1
    return float_array
        
