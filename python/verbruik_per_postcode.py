import pickle as pl
from bokeh.plotting import figure
from bokeh.io import output_file, show
from csv_utils import *

# create lists of postcodes

save_location = get_deliverables_path()
postcodes = []
for i in range (1000, 1183):
    postcodes.append(str(i))
years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

for year in years:
    gas_pd = get_pandas('GAS_' + year + '.csv') 
    el_pd = get_pandas('ELK_' + year + '.csv') 
    el_x_as = []
    el_y_as = []
    gas_x_as = []
    gas_y_as = []
    for postcode in postcodes:
        gas_pc_sjv = gas_pd[gas_pd['POSTCODE_VAN'].str.contains(postcode)]
        el_pc_sjv = el_pd[el_pd['POSTCODE_VAN'].str.contains(postcode)]
        if(sum(gas_pc_sjv['Aantal Aansluitingen']) != 0):
            elsumSJV = el_pc_sjv['SJV'] * el_pc_sjv['Aantal Aansluitingen']
            if(sum(elsumSJV) != 0):
                el_x_as.append(postcode)
                el_y_as.append(sum(elsumSJV) / sum(el_pc_sjv['Aantal Aansluitingen']) )

            gassumSJV = gas_pc_sjv['SJV'] * gas_pc_sjv['Aantal Aansluitingen']
            if(sum(gassumSJV) != 0):
                gas_x_as.append(postcode)
                gas_y_as.append(sum(gassumSJV) / sum(gas_pc_sjv['Aantal Aansluitingen']) )

    file_name = "elektra" + year + ".html"
    output_file(save_location / 'week2' / file_name)
    p = figure(x_range=el_x_as, plot_height=1000, title="Elektra per postcode-4 " + year)
    p.vbar(x=el_x_as, top=el_y_as, width=1)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)

    file_name = "gas" + year + ".html"
    output_file(save_location / 'week2' / file_name)
    p = figure(x_range=gas_x_as, plot_height=1000, title="Gas per postcode-4 " + year)
    p.vbar(x=gas_x_as, top=gas_y_as, width=1)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)
