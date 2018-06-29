import numpy as np
from sklearn.manifold import TSNE
from csv_utils import *
import matplotlib.pyplot as plt
from catagorize_postalcode import get_numeric_postal

data = get_pandas("GAS_2018.csv")
# put this in t-sne
sjv = data["SJV"]
aantalaan = data["Aantal Aansluitingen"]
perc = get_clean_data(list(data['%Leveringsrichting']))
post = get_numeric_postal(data["POSTCODE_VAN"])

tsne_data = np.ndarray(shape=(len(post),4), dtype=float, order='F')

for i in range(len(post)):
    tsne_data[i] = np.array([sjv[i], aantalaan[i], perc[i], post[i]])

X = np.array(tsne_data)


X_embedded = TSNE(n_components=2).fit_transform(X)

c = ['red', 'green', 'blue', 'yellow', 'purple']
colors = []
for i in range(len(X)):
    if i < len(X) / 5:
        colors.append('red')
    if i < 2 * len(X) / 5:
        colors.append('green')
    if i < 3 * len(X) / 5:
        colors.append('blue')
    if i < 4 * len(X) / 5:
        colors.append('yellow')
    if i < len(X):
        colors.append('purple')
    colors.append

plt.scatter(X_embedded[:,0], X_embedded[:,1], c = colors)
plt.show()