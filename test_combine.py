import pandas as pd
import matplotlib.pyplot as plt


df_cmpt_demo = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt_bydemo.json')
df_cmpt = pd.read_json('JSON_data_files/2019_suicidepct_bycmpt.json', typ='series')
df_cmpt = df_cmpt.to_frame()
df_cmpt.columns=['pct']

soldier_data = pd.read_csv('Soldier_data_fake copy.csv')

class Roster:
    '''Creates a dictionary of patient data'''
    def __init__(self, dataframe):
        dataframe['dodid'] = dataframe['dodid'].fillna(0).astype('int')
        dataframe = dataframe.set_index('dodid')
        self.roster = dataframe.to_dict(orient = 'index')
        
    def __str__(self):
        return str(self.roster)

class Display():
    '''Assumes this class is passed a value (soldier) from the roster dictionary, where 
        the value contains soldier data and was accessed using DODID dictionary key.
        '''
    def __init__(self, soldier):
        self.fig, self.ax = plt.subplots(2, 2, figsize=(15,7))
        self.fig.subplots_adjust(hspace=.25)

        if soldier['status'] == 'AD':
            active_byage = df_cmpt_demo['17-19':'55-59']['Active']*100
            active_bybranch = df_cmpt['All Active':'Air Force']*100
            active_bysex = df_cmpt_demo['Male':'Female']['Active']*100
            active_bygrade = df_cmpt_demo["All Enlisted":"Cadet"]['Active']*100
            self.ax = self.create_display('Active Duty', active_byage, active_bybranch, active_bysex, active_bygrade)

        elif soldier['status'] == 'Reserve':
            reserve_byage = df_cmpt_demo['17-19':'55-59']['Reserve']*100
            reserve_bybranch = df_cmpt['All Reserve':'Air Force Reserve']*100
            reserve_bysex = df_cmpt_demo['Male':'Female']['Reserve']*100
            reserve_bygrade = df_cmpt_demo["All Enlisted":"Cadet"]['Reserve']*100
            self.ax = self.create_display('Reserve', reserve_byage, reserve_bybranch, reserve_bysex, reserve_bygrade)

        elif soldier['status'] == 'NG':
            guard_byage = df_cmpt_demo['17-19':'55-59']['National Guard']*100
            guard_bybranch = df_cmpt['All National Guard':'Air National Guard']*100
            guard_bysex = df_cmpt_demo['Male':'Female']['National Guard']*100
            guard_bygrade = df_cmpt_demo["All Enlisted":"Cadet"]['National Guard']*100
            self.ax = self.create_display('National Guard', guard_byage, guard_bybranch, guard_bysex, guard_bygrade)

        else: 
            pass
            # SEND TO ERROR CLASS, branch data not available

    def create_display(self, status, age, branch, sex, grade):

        ### PLOT 1: RISK BY COMPONENT ###
        self.ax[0,0].bar(branch.index, branch.pct)
        self.ax[0,0].set_title("% of Service Member Suicides by Specific Component, 2019")
        self.ax[0,0].set_ylabel("% of suicides")
        self.ax[0,0].set_xlabel(status +  " Component")

        ### PLOT 2: RISK BY AGE ###
        self.ax[0,1].bar(age.index, age.values)
        self.ax[0,1].set_title("% of " + status + " Suicides by Age, 2019") 
        self.ax[0,1].set_ylabel("% of suicides")
        self.ax[0,1].set_xlabel("Service Member Age")

        ### PLOT 3: RISK BY SEX ###
        self.ax[1,1].bar(sex.index, sex.values)
        self.ax[1,1].set_title("% of " + status + " Suicides by Sex, 2019") 
        self.ax[1,1].set_ylabel("% of suicides")
        self.ax[1,1].set_xlabel("Sex of Service Member")

        ### PLOT 4: RISK BY GRADE ###
        self.ax[1,0].bar(grade.index, grade.values)
        self.ax[1,0].set_title("% of " + status + " Suicides by Grade, 2019") 
        self.ax[1,0].set_ylabel("% of suicides")
        self.ax[1,0].set_xlabel("Grade of Service Member")

        self.highlight_soldier(status)
        plt.show()

ros = Roster(soldier_data)
soldier = ros.roster[4389679928]
display = Display(soldier)

print(len(ros.roster))
