from csv_utils import *
import pickle as pl
from pathlib import Path

# get usefull columns of the yearly data and save as processed arrays
save_dir = get_data_path('processed')

# years to analyse
years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
def process_average_yearly_gas_elektra():
    gas = {}
    electra = {}
    for year in years:
        # save description of gas usage
        gas_pd = get_pandas('GAS' + '_' + year + '.csv') 
        gas_averaged_sjv = gas_pd['SJV'] / gas_pd['Aantal Aansluitingen']
        print(gas_averaged_sjv.mean(), gas_averaged_sjv.std())
        gas[int(year)] = gas_averaged_sjv.mean()
    
        el_pd = get_pandas('ELK' + '_' + year + '.csv') 
        el_averaged_sjv = el_pd['SJV'] / el_pd['Aantal Aansluitingen']
        print(el_averaged_sjv.mean(), el_averaged_sjv.std())
        electra[int(year)] = el_averaged_sjv.mean()

    with open(save_dir / '/average_yearly_gas_usage_2009_2018.pickle', 'wb') as out:
        pl.dump(gas, out, protocol=pl.HIGHEST_PROTOCOL)
    
    with open(save_dir / '/average_yearly_elk_usage_2009_2018.pickle', 'wb') as out:
        pl.dump(electra, out, protocol=pl.HIGHEST_PROTOCOL)

# process_average_yearly_gas_elektra()

# test
'''
with open(save_dir + '/average_yearly_elk_usage_2009_2018.pickle', 'rb') as fl:
    elk = pl.load(fl)

with open(save_dir + '/average_yearly_gas_usage_2009_2018.pickle', 'rb') as fl:
    gas = pl.load(fl)

for year in years:
    print(year, 'gas: ', gas[year], 'elect: ', elk[year])
'''

def get_yearly_power_consumption(year):
    gas_pd = get_pandas('GAS' + '_' + year + '.csv') 
    elk_pd = get_pandas('ELK' + '_' + year + '.csv')

    gas_usage = np.array(gas_pd['SJV'] / gas_pd['Aantal Aansluitingen'])
    elk_usage = np.array(elk_pd['SJV'] / elk_pd['Aantal Aansluitingen'])

    with open(save_dir / ''.join(('gas_per_aansluiting', year, '.pickle')), 'wb') as out:
        pl.dump(gas_usage, out, protocol=pl.HIGHEST_PROTOCOL)
    
    with open(save_dir / ''.join(('elk_per_aansluiting', year , '.pickle')), 'wb') as out:
        pl.dump(elk_usage, out, protocol=pl.HIGHEST_PROTOCOL)

get_yearly_power_consumption('2018')