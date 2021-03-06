from csv_utils import *
import pickle as pl
import matplotlib.pylab as plt

# load the data for the plots
data_path = get_data_path('processed')



with open(data_path + '/average_yearly_elk_usage_2009_2018.pickle', 'rb') as fl:
    elc_data = pl.load(fl)

with open(data_path + '/scaled_average_yearly_elk_usage_2009_2018.pickle', 'rb') as fl:
    scaled_elc_data = pl.load(fl)

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

def save_dict_bar_plot(dict_list, title, plot_names_list, axis_labels):
    '''
    plots dicts in one plot, dict_list can have multiple dict objects.
    The keys of the dict are plotted on the x and the values on the y axis.
    Provide title and the names of the plots.
    '''
    for i in range(len(dict_list)):
        lists = sorted(dict_list[i].items()) # sorted by key, return a list of tuples

        x, y = zip(*lists) # unpack a list of pairs into two tuples

        plt.bar(x, y, label = plot_names_list[i])
    plt.xlabel(axis_labels[0])
    plt.ylabel(axis_labels[1])
    plt.legend(loc = 'lower right')
    plt.title(title)
    plt.savefig(save_location + 'week2/' + title, bbox_inches='tight')
    plt.close()

# example usage (uncomment to run)
# save_dict_bar_plot([scaled_elc_data, gas_data], 'Gemiddeld verbuik van gas en electra in amsterdam per jaar bar plot', ['Electra in KWh', 'Gas in m^3'], ['Jaar', 'Verbruik'])
# save_dict_bar_plot([gas_data], 'Gemiddeld verbuik van gas in amsterdam per jaar bar plot', ['Gas in m^3'], ['Jaar', 'Verbruik'])
# save_dict_bar_plot([scaled_elc_data], 'Gemiddeld verbuik van electra in amsterdam per jaar bar plot', ['Electra in KWh.'], ['Jaar', 'Verbruik'])
# save_dict_bar_plot([scaled_elc_data, elc_data], 'Gemiddeld verbuik en levering van electra in amsterdam per jaar', ['Electra totaal','Electra geleverd'], ['Jaar', 'Verbruik electra KWh'])


def save_hist_plot(data_name, title, x_label):
    with open(data_path + '/' + data_name, 'rb') as fl:
        hist_data = pl.load(fl)
    mean = hist_data.mean()
    std = hist_data.std()
    plt.hist(hist_data, bins = 100)
    plt.title(title)
    plt.xlabel(x_label)
    plt.axvline(mean, label = 'mean', color='k', linestyle='dashed', linewidth=1)
    plt.axvline(mean - std, label = 'mean - 1 sigma' ,color='r', linestyle='dashed', linewidth=1)
    plt.axvline(mean + std, label = 'mean + 1 sigma' ,color='b', linestyle='dashed', linewidth=1)
    plt.legend()
    plt.savefig(save_location + 'week2/' + title, bbox_inches='tight')    
    plt.close()

# uncomment to run
# save_hist_plot('elk_per_aansluiting2018.pickle', 'Electra geleverd per aansluiting 2018', 'Geleverde electra per aansluiting in KWh')
# save_hist_plot('gas_per_aansluiting2018.pickle', 'Gas verbruik per aansluiting 2018', 'Verbruik per aansluiting in m^3')

# logarithm of consumption
# save_hist_plot('log_elk_per_aansluiting2018.pickle', 'Logaritme geleverde electra per aansluiting 2018', 'log(geleverd) per aansluiting in KWh')
# save_hist_plot('log_gas_per_aansluiting2018.pickle', 'Logaritme gas verbruik per aansluiting 2018', 'log(verbruik) per aansluiting in m^3')

def plot_two_scales(dict_one, dict_two, labels):
    plot_left = sorted(dict_one.items()) 
    x_l, y_l = zip(*plot_left) 
    plot_right = sorted(dict_two.items()) 
    x_r, y_r = zip(*plot_right)
    x_r = np.array(x_r) - 1
    fig, ax1 = plt.subplots()
    
    ax1.bar(x_l, y_l)
    ax1.set_xlabel('year')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel(labels[0], color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(x_r, y_r, 'r.')
    ax2.set_ylabel(labels[1], color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    plt.title('Gemiddelde temperatuur en gasverbruik 2008 - 2017')
    plt.show()

def plot_difference(dict_one, dict_two, title, plot_names, axis):
    difference = {}
    for key in dict_one:
        difference[key] = dict_one[key] - dict_two[key]
    save_dict_bar_plot([difference], title, plot_names, axis)


with open(data_path + '/gemiddelde_temperatuur_2008_2017.pickle', 'rb') as fl:
    temp_data = pl.load(fl)


# uncomment to run
plot_difference(scaled_elc_data, elc_data, "Gemiddelde Opgewekte energie per jaar", ["Verschil electra totaal min geleverd"], ["Jaar", "Opgewekte electra KWh"])

# plot_two_scales(temp_data, gas_data, ['Jaarlijks gemiddelde temperatuur Schiphol graden Celcius','Jaarlijks gemiddeld gas verbruik Amsterdam in m^3'])