
import re
import pandas as pd
from datetime import datetime

soldier_data = pd.read_csv('Soldier_data_fake1_20210409 copy.csv')

class Roster:
    '''Creates a dictionary of patient data'''
    def __init__(self, dataframe):
        dataframe['dodid'] = dataframe['dodid'].fillna(0).astype('int')
        dataframe = dataframe.set_index('dodid')
        self.roster = dataframe.to_dict(orient = 'index')
        
    def __str__(self):
        return str(self.roster)

ros = Roster(soldier_data)

# soldier = ros.roster[4389679928]
# print(soldier)

print(soldier_data.grade)


# age_days = datetime.today().date() - datetime.strptime(soldier['dob'] + ' 00:00:00', '%m/%d/%Y' + ' %H:%M:%S' ).date()
# age = age_days.days/365
# bar = '18-30'
# print(bar[0:2])
# print(bar[3:])
# print(age in range(int(bar[0:2]),int(bar[3:])))