#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:18 2021

@author: denise
"""
import csv
import pandas as pd

data = pd.read_csv (r"Soldier_data_fake.csv")

for row in data:
    print row[12]

class Data:
    def createAccount():
        
        account_name = raw_input('Enter login: ')
        password = enterPassword()
        appendAccount('Soldier_data_fake.csv', username, password)

def enterPassword():
  while True: 
    password = raw_input('Enter password: ')
    password_again = raw_input('Confirm password: ')
    if len(password) < 5: # or whatever sanity check you might like
      print ('Your password is too short.')
    elif password != password_again:
      print('Password and confirmation do not match.')
    else:
      return password
      # all is well; 'return' breaks the loop



# =============================================================================
# data.set_index ("DODID", inplace=True)
#         verify1 = int(input ("Please enter your full DODID number with do dashes or spaces: "))
#         for index, row in data.iterrows ():
#             if row['DODID'] == verify1:
#                 print ("Please wait while page loads.")
#             else:
#                 raise Invalid_DODID
#                 # verify2 = str(input("Please verify your DOB in MM/DD/YYYY format: "))
#         # to ensure right data is loading
#         # login_info = line.split()
# 
# 
#     while True:
#         confirm = input (f'Your email address on file is: {}, and you phone number is {} is this correct? Y or N ').format (EMAIL, PHONE).upper()
#         if confirm == "N":
#             confirm2 = input("Would you like to update now? Y or N").upper()
#             if confirm2 == "Y":
#                 confirm3 = input("Press 1 to update your phone number; press 2 to update your email address.")
#                 if confirm3 == "1":
#                     appended.PHONE
#                 elif confirm3 == "2":
#                     append.EMAIL
#                 else:
#                     Raise Exception as Error_Email
#             else:
#                 if confirm2 == "N":
#                  break
# 
#                else: Raise Exception as Error_Phone
# 
#         elif: confirm == "Y":
#         break
#         else:
# =============================================================================
