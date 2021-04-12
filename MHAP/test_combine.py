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
            self.ax = self.create_display('Active Duty', active_byage, active_bybranch, active_bysex, active_bygrade, soldier)

        elif soldier['status'] == 'Reserve':
            reserve_byage = df_cmpt_demo['17-19':'55-59']['Reserve']*100
            reserve_bybranch = df_cmpt['All Reserve':'Air Force Reserve']*100
            reserve_bysex = df_cmpt_demo['Male':'Female']['Reserve']*100
            reserve_bygrade = df_cmpt_demo["All Enlisted":"Cadet"]['Reserve']*100
            self.ax = self.create_display('Reserve', reserve_byage, reserve_bybranch, reserve_bysex, reserve_bygrade, soldier)

        elif soldier['status'] == 'NG':
            guard_byage = df_cmpt_demo['17-19':'55-59']['National Guard']*100
            guard_bybranch = df_cmpt['All National Guard':'Air National Guard']*100
            guard_bysex = df_cmpt_demo['Male':'Female']['National Guard']*100
            guard_bygrade = df_cmpt_demo["All Enlisted":"Cadet"]['National Guard']*100
            self.ax = self.create_display('National Guard', guard_byage, guard_bybranch, guard_bysex, guard_bygrade, soldier)

        else: 
            pass
            # SEND TO ERROR CLASS, branch data not available

    def create_range(string):
    	return range(int(string[0:2]),int(string[3:]))

    def create_display(self, status, age, branch, sex, grade, soldier):
        
        ### PLOT 1: RISK BY COMPONENT ###
        color_branch = []
        [color_branch.append('red') if (soldier['branch'] == item[0:4]) else color_branch.append('cornflowerblue') for item in branch.index[1:]]
        self.ax[0,0].bar(branch.index[1:], branch.pct[1:], color = color_branch)
        self.ax[0,0].set_title("% of Service Member Suicides by Specific Component, 2019", fontweight = 'bold')
        self.ax[0,0].set_ylabel("% of suicides")
        self.ax[0,0].set_xlabel(status +  " Component")
        

        ### PLOT 2: RISK BY AGE ###
        colors = []
        age_days = datetime.today().date() - datetime.strptime(soldier['dob'] + ' 00:00:00', '%m/%d/%y' + ' %H:%M:%S' ).date()
        soldier_age = age_days.days/365
        ranges = pd.Series(age.index).apply(Display.create_range)
        [colors.append('red') if (math.floor(soldier_age) in item) else colors.append('cornflowerblue') for item in ranges ]  

        self.ax[0,1].bar(age.index, age.values, color = colors)
        self.ax[0,1].set_title("% of " + status + " Suicides by Age, 2019", fontweight = 'bold') 
        self.ax[0,1].set_ylabel("% of suicides")
        self.ax[0,1].set_xlabel("Service Member Age")
        
        
        ### PLOT 3: RISK BY SEX ###
        if soldier['gender'] == 'f':
            self.ax[1,1].bar(sex.index, sex.values, color = ['cornflowerblue','red'])
        else:
            self.ax[1,1].bar(sex.index, sex.values, color = ['red','cornflowerblue'])
        self.ax[1,1].set_title("% of " + status + " Suicides by Sex, 2019", fontweight = 'bold') 
        self.ax[1,1].set_ylabel("% of suicides")
        self.ax[1,1].set_xlabel("Sex of Service Member")
        
        
        ### PLOT 4: RISK BY GRADE ###
        colors_grade = []
        for item in grade.index[1:]:
            if (item == 'E1-E4') & (soldier['grade'].upper() in ['E1', 'E2', 'E3', 'E4']):
                colors_grade.append('red')
            elif (item == 'E5-E9') & (soldier['grade'].upper() in ['E5', 'E6', 'E7', 'E8', 'E9']):
                colors_grade.append('red')
            elif (item == 'O1-O9') & (soldier['grade'][0] == 'o'):
                colors_grade.append('red')
            elif (item == 'W1-W5') & (soldier['grade'][0] == 'w'):
                colors_grade.append('red')
            elif (item == 'Cadet') & (soldier['grade'][0] == 'c'):
                colors_grade.append('red')
            else:
                colors_grade.append('cornflowerblue')
                
        
        self.ax[1,0].bar(grade.index[1:], grade.values[1:], color = colors_grade)
        self.ax[1,0].set_title("% of " + status + " Suicides by Grade, 2019", fontweight = 'bold') 
        self.ax[1,0].set_ylabel("% of suicides")
        self.ax[1,0].set_xlabel("Grade of Service Member")
        self.ax[1,0].tick_params(axis = 'x',rotation=35)
        
        plt.suptitle(soldier['l_name'] + ', ' + soldier['f_name'], fontsize = 20)
        # Helps with the spacing between subplots
        plt.tight_layout()
        plt.show()

ros = Roster(soldier_data)
print(list(ros.roster.keys()))
id = int(input('Enter a dodid from above to see the data ', ))

####FOR DENISE if dod id not in dict, Key Error
soldier = ros.roster[id]
display = Display(soldier)
print(len(ros.roster))





