import pandas as pd

data = pd.read_csv('Soldier_data_fake copy.csv')

class Roster:
    '''Creates a dictionary of patient data'''
    def __init__(self, dataframe):
        dataframe['dodid'] = dataframe['dodid'].fillna(0).astype('int')
        dataframe = dataframe.set_index('dodid')
        self.roster = dataframe.to_dict(orient = 'index')
        
    def __str__(self):
        return str(self.roster)

ros = Roster(data)

print(len(ros.roster))
