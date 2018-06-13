from csv_utils import *
import pickle as pl
import matplotlib.pylab as plt

# load the data for the plots
data_path = get_data_path('processed')

with open(data_path + '/average_yearly_elk_usage_2009_2018.pickle', 'rb') as fl:
    elc_data = pl.load(fl)

with open(data_path + '/average_yearly_gas_usage_2009_2018.pickle', 'rb') as fl:
    gas_data = pl.load(fl)

# save plots here
save_location = get_deliverables_path()

def save_dict_plot(dict_list, title, plot_names_list, axis_labels):
    '''
    plots dicts in one plot, dict_list can have multiple dict objects.
    The keys of the dict are plotted on the x and the values on the y axis.
    Provide title and the names of the plots.
    '''
    for i in range(len(dict_list)):
        lists = sorted(dict_list[i].items()) # sorted by key, return a list of tuples

        x, y = zip(*lists) # unpack a list of pairs into two tuples

        plt.plot(x, y, label = plot_names_list[i])
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.legend()
    plt.title(title)
    plt.savefig(save_location + 'week2/' + title, bbox_inches='tight')


save_dict_plot([elc_data, gas_data], 'Gemiddeld verbuik van gas en electra in amsterdam per jaar', ['Electra in KWh', 'Gas in m^3'], ['Jaar', 'Verbruik'])
