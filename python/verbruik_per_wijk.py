import pickle as pl
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from csv_utils import *

# lijst met postcodes

save_location = get_deliverables_path()

def postcodelijst(van = 1000, tot = 1182):
    postcodelijst = []
    for i in range (van, tot + 1):
        postcodelijst.append(str(i))
    return postcodelijst

def years(van = 2009, tot = 2018):
    years = []
    for i in range (van, tot + 1):
        years.append(str(i))
    return years

def wijkplot(wijk, postcodes):
    jaren = years()
    
    eldata = {'postcodes' : postcodes}
    gasdata = {'postcodes' : postcodes}
    if(postcodes == ['1099', '1114']):
        eldata['postcodes'] = ['1099/1114']
        gasdata['postcodes'] = ['1099/1114']
    
    for year in jaren:
        gas_pd = get_pandas('GAS_' + year + '.csv') 
        el_pd = get_pandas('ELK_' + year + '.csv') 

        el_postcodes = []
        el_y_as = []
        gas_postcodes = []
        gas_y_as = []
        for postcode in postcodes:
            gas_pc_sjv = gas_pd[gas_pd['POSTCODE_VAN'].str.contains(postcode)]
            el_pc_sjv = el_pd[el_pd['POSTCODE_VAN'].str.contains(postcode)]
            if(sum(gas_pc_sjv['Aantal Aansluitingen']) != 0):
                elsumSJV = el_pc_sjv['SJV'] * el_pc_sjv['Aantal Aansluitingen']
                el_postcodes.append(postcode)
                el_y_as.append(sum(elsumSJV) / sum(el_pc_sjv['Aantal Aansluitingen']) )
                gassumSJV = gas_pc_sjv['SJV'] * gas_pc_sjv['Aantal Aansluitingen']
                gas_postcodes.append(postcode)
                gas_y_as.append(sum(gassumSJV) / sum(gas_pc_sjv['Aantal Aansluitingen']) )
        eldata[year] = el_y_as
        gasdata[year] = gas_y_as
    
    if(postcodes == ['1099', '1114']):
         postcodes = ['1099 / 1114']

    filename = "Elektra" + wijk + ".html"
    output_file(save_location / 'week2' / filename)
    x = [ (postcode, year) for postcode in postcodes for year in jaren ]
    counts = sum(zip(eldata['2009'], eldata['2010'], eldata['2011'], eldata['2012'] , eldata['2013'], eldata['2014'], eldata['2015'], eldata['2016'], eldata['2017'], eldata['2018']), ())
    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=500, plot_width=1500, title="Elektriciteitsverbruik per postcode-4 in" + wijk, toolbar_location=None, tools="")
    p.vbar(x='x', top='counts', width=0.9, source=source)
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    show(p)

    filename = "Gas" + wijk + ".html"
    output_file(save_location / 'week2' / filename)
    x = [ (postcode, year) for postcode in postcodes for year in jaren ]
    counts = sum(zip(gasdata['2009'], gasdata['2010'], gasdata['2011'], gasdata['2012'] , gasdata['2013'], gasdata['2014'], gasdata['2015'], gasdata['2016'], gasdata['2017'], gasdata['2018']), ())
    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=500, plot_width=1500, title="Gasverbruik per Postcode-4 in " + wijk , toolbar_location=None, tools="")
    p.vbar(x='x', top='counts', width=0.9, source=source)
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    show(p)


#    filename = "Elektra" + wijk + ".html"
#    output_file(save_location / 'week2' / filename)
#    source = ColumnDataSource(data=dict(x=el_x_as, counts=el_dict))
#    p = figure(x_range=el_x_as, plot_height=1000, title="Elektra per postcode-4 " + year)
#    p.vbar(x=el_x_as, top=el_y_as, width=0.8)
#    p.xgrid.grid_line_color = None
#    p.y_range.start = 0
#    show(p)

#    filename = "Gas" + wijk + ".html"
#    output_file(save_location / 'week2' / filename)
#    source = ColumnDataSource(data=dict(x=gas_x_as, counts=gas_y_as))
#    p = figure(x_range=gas_x_as, plot_height=1000, title="Gas per postcode-4 " + year)
#    p.vbar(x=gas_x_as, top=gas_y_as, width=0.8)
#    p.xgrid.grid_line_color = None
#    p.y_range.start = 0
#    show(p)

wijkplot("Amsterdam-Centrum", postcodelijst(1011, 1018))
wijkplot("Oostelijk-Havengebied", ['1019'])
wijkplot("Amsterdam-Noord", ['1021', '1022', '1023', '1024', '1025', '1026', '1027', '1028', '1031', '1032', '1033', '1034', '1035', '1036', '1037'])
wijkplot("Amsterdam-Westpoort", ['1041', '1042', '1043', '1045', '1046', '1047'])
wijkplot("Amsterdam-West", postcodelijst(1051, 1059))
wijkplot("Amsterdam-Nieuw-West", postcodelijst(1060, 1069))
wijkplot("Amsterdam-Zuid", ['1071', '1072', '1073', '1074', '1075', '1076', '1077', '1078', '1079', '1081', '1082', '1083'])
wijkplot("Amsterdam-Oost", ['1086', '1091', '1092', '1093', '1094', '1095', '1096', '1097', '1098'])
wijkplot("Amsterdam-Zuidoost", postcodelijst(1101, 1108))
wijkplot("Driemond", ['1109'])
wijkplot("Amsterdam-Duivendrecht", ['1099', '1114'])