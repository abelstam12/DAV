import os
import pandas as pd

def get_data_path(filename):
    current_path = os.getcwd().split('/')
    return '/'.join(current_path[0:-1]) + '/Data' + '/' + filename

def get_pandas(filename, encoding='LATIN-1', sep = ';'):
    return pd.read_csv(get_data_path(filename), encoding = encoding, sep = sep)

