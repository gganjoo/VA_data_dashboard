from datetime import datetime
import math
import pandas as pd
import matplotlib.pyplot as plt


df_cmpt_demo = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt_bydemo.json')
df_cmpt = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt.json', typ='series')
df_cmpt = df_cmpt.to_frame()
df_cmpt.columns=['pct']

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
print(list(ros.roster.keys()))
id = int(input('Enter a dodid from above to see the data ', ))

####FOR DENISE if dod id not in dict, Key Error
soldier = ros.roster[id]
display = Display(soldier)
print(len(ros.roster))