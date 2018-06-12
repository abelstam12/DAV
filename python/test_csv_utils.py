from csv_utils import *

# haal 'kleinverbruikamsterdam2018' op uit de data map
pd = get_pandas('kleinverbruikamsterdam2018.csv')

# print de kollommen als lijst
print(pd.columns.tolist())

#print de eerste 100 entries van de kolom 'MEETVERANTWOORDELIJKE'
print(get_float(pd['%SJV laag tarief'][0:100]))
