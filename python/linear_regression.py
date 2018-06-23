from csv_utils import *
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from catagorize_postalcode import *

# load electricity and gas data
gas_pd = get_pandas('GAS_2018.csv') 
elk_pd = get_pandas('ELK_2018.csv')

save_location = get_deliverables_path()

def plot_x_y(plot_x, plot_y, title, axis):
    plt.plot(plot_x, plot_y, 'o')
    plt.title(title)
    plt.xlabel(axis[0])
    plt.ylabel(axis[1])
    #plt.savefig(save_location + 'week2/' + title, bbox_inches='tight')
    plt.show()
    return

def get_numeric_postal(pd_postal_column):
    pc = np.array(pd_postal_column)
    for index in range(len(pc)):
        pc[index] = int(pc[index][0:4])
    return pc

def lin_regres(explanetory, to_explain):
    # Use only one feature
    #post_array = get_numeric_postal(gas_pd["POSTCODE_VAN"])
    #aansluiting_array = np.array(gas_pd["Aantal Aansluitingen"])
    diabetes_X = explanetory.reshape(-1, len(explanetory))
    #diabetes_X = np.array([post_array, aansluiting_array]).reshape(-1, 2)
    diabetes_y = np.array(to_explain).reshape(-1, 1)

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
        % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))



# plot_x_y(get_numeric_postal(gas_pd['POSTCODE_VAN']), gas_pd['SJV'], 'Verbruik gas tegen postcode', ['Postcode','Verbruik in m^3'])
# plot_x_y(gas_pd['Aantal Aansluitingen'], gas_pd['SJV'], 'Verbruik_gas_tegen_het_aantal_aansluitingen', ['Aantal aansluitingen', 'Verbruik m^3'])
# plot_x_y(get_numeric_postal(elk_pd['POSTCODE_VAN']), elk_pd['SJV'], 'Verbruik gas tegen postcode', ['Postcode','Verbruik in m^3'])
# plot_x_y(elk_pd['Aantal Aansluitingen'], elk_pd['SJV'], 'Verbruik_gas_tegen_het_aantal_aansluitingen', ['Aantal aansluitingen', 'Verbruik m^3'])

post = catagorized_postal(elk_pd["POSTCODE_VAN"])
exp = np.array([post[1]])
lin_regres(np.array([post[1]]), elk_pd["SJV"])