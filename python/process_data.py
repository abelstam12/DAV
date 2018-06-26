from csv_utils import *
import pickle as pl

# get usefull columns of the yearly data and save as processed arrays
save_dir = get_data_path('processed')

# years to analyse
years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
def process_average_yearly_gas_elektra():
    '''
    Get yealy scaled averages and save the data in the processed data repos.
    '''
    gas = {}
    electra = {}
    for year in years:
        # get and save all the data for each year.
        gas_pd = get_pandas('GAS' + '_' + year + '.csv') 
        gas_averaged_sjv = ( gas_pd['SJV'] * gas_pd['Aantal Aansluitingen'] ) / gas_pd['Aantal Aansluitingen'].sum()
        gas[int(year)] = gas_averaged_sjv.sum()
    
        el_pd = get_pandas('ELK' + '_' + year + '.csv') 
        el_averaged_sjv = (el_pd['SJV'] * el_pd['Aantal Aansluitingen']) / el_pd['Aantal Aansluitingen'].sum()
        electra[int(year)] = el_averaged_sjv.sum()

    with open(save_dir + '/average_yearly_gas_usage_2009_2018.pickle', 'wb') as out:
        pl.dump(gas, out, protocol=pl.HIGHEST_PROTOCOL)
    
    with open(save_dir + '/average_yearly_elk_usage_2009_2018.pickle', 'wb') as out:
        pl.dump(electra, out, protocol=pl.HIGHEST_PROTOCOL)



def get_yearly_power_consumption(year):
    gas_pd = get_pandas('GAS' + '_' + year + '.csv') 
    elk_pd = get_pandas('ELK' + '_' + year + '.csv')

    gas_usage = np.array(gas_pd['SJV'] )
    gas_aansluitingen = np.array(gas_pd['Aantal Aansluitingen'] )
    elk_usage = np.array(elk_pd['SJV'] )
    elk_aansluitingen = np.array(elk_pd['Aantal Aansluitingen'] )

    all_sjv_gas = []
    all_sjv_elk = []
    for i in range(len(gas_usage)):
        all_sjv_gas.extend([gas_usage[i]] * gas_aansluitingen[i])
    for i in range(len(elk_usage)):
        all_sjv_elk.extend([elk_usage[i]] * elk_aansluitingen[i])
    print(len(all_sjv_gas), len(all_sjv_elk))
    with open(save_dir + '/gas_per_aansluiting' + year + '.pickle', 'wb') as out:
        pl.dump(gas_usage, out, protocol=pl.HIGHEST_PROTOCOL)
    
    with open(save_dir + '/elk_per_aansluiting' + year + '.pickle', 'wb') as out:
        pl.dump(elk_usage, out, protocol=pl.HIGHEST_PROTOCOL)

def get_scaled_elec_usage():
    electra = {}
    for year in years:
        el_pd = get_pandas('ELK' + '_' + year + '.csv') 
        scaling = get_clean_data(list(el_pd['%Leveringsrichting']))
        print(len(list(el_pd['%Leveringsrichting'])), scaling.shape, year)
        el_averaged_sjv_scaled = np.array(el_pd['SJV'] * el_pd['Aantal Aansluitingen'] ) / (scaling / 100.)
        el_averaged_sjv_scaled = (el_averaged_sjv_scaled) / el_pd['Aantal Aansluitingen'].sum()
        electra[int(year)] = el_averaged_sjv_scaled.sum()

    with open(save_dir + '/scaled_average_yearly_elk_usage_2009_2018.pickle', 'wb') as out:
        pl.dump(electra, out, protocol=pl.HIGHEST_PROTOCOL)




def get_average_yearly_temperature():
    # pandas loads the data as one column, so the processing needs 
    # a different approach
    temp_data = get_pandas('KNMI_20171231.csv')
    data_out = {
        2008: [], 2009: [], 2010: [], 2011: [], 2012: [], 2013: [], 
        2014: [], 2015: [], 2016: [], 2017: []
    }
    norm = len(temp_data)
    for index, row in temp_data.iterrows():
        row_to_list = list(row)[0].split(',')
        year = int(row_to_list[1][:4])
        temperature = float(row_to_list[2].replace(" ", "")) / 10
        data_out[year].append(temperature)
    for key in data_out.keys():
        # creative way to get average temp
        data_out[key] = np.sum(np.array(data_out[key]) / len(data_out[key]))
    print(index)
    print(data_out)
    with open(save_dir + '/gemiddelde_temperatuur_2008_2017' + '.pickle', 'wb') as out:
        pl.dump(data_out, out, protocol=pl.HIGHEST_PROTOCOL)

# uncomment to process
# process_average_yearly_gas_elektra()
# get_scaled_elec_usage()
# get_yearly_power_consumption('2018')
# process_average_yearly_gas_elektra()
# get_average_yearly_temperature()