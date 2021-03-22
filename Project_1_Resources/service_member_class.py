#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:32:25 2021

@author: denise
"""

from datetime import datetime
import pandas as pd

data = pd.read_csv (r'Soldier_data_fake.csv')
data1 = pd.read_csv(r'SPN_Codes.cvs')
from mapping import LAST_NAME, FIRST_NAME, MIDDLE_INITIAL, SUFFIX, DOB, GENDER, DODID, EMAIL, PHONE, ADDRESS, \
    NOK_NAME, NOK_PHONE, NOK_ADDRESS, BRANCH, STATUS, DESIGNATOR, COC, ETS, BASD, GRADE, SPN

class Error(Exception):
    #em = error message
    pass

class Invalid_DODID(Error):
    def __init__(self, em1):
        self.em1 = em1
        return("You have not entered a valid DODID, please try again. If you think you have received this message in error please contact your local HR or VA office.")

    def __str__(self):
        return em1

class Invalid_Input(Error):
    def __init__(self, em2):
        self.em2 = em2
        return("Invalid input, please try again.")

    def __str__(self):
        return em2

class Error_Email(Error):
    def __init__(self, em3):
        self.em3 = em3
        return("Invalid email input, please enter your email address, for example john.Doe22@outlook.com")

    def __str__(self):
        return em3

class Error_Phone(Error):
    def __init__(self, em4):
        self.em4 = em4
        return("Invalid email input, please enter your phone number with no dashes, for example 5201234567")

    def __str__(self):
        return em4


class Person (object):
    def __init__(self, LAST_NAME, FIRST_NAME, MIDDLE_INITIAL, SUFFIX, DOB, GENDER, DODID, CONTACT_INFO, SM_INFO):
        self.LAST_NAME = LAST_NAME
        self.FIRST_NAME = FIRST_NAME
        self.MIDDLE_INITIAL = MIDDLE_INITIAL
        self.SUFFIX = SUFFIX
        self.DOB = DOB
        self.GENDER = GENDER
        self.DODID = DODID
        data.set_index ("DODID", inplace=True)
        # indexing by DODID to ensure that information is pulled from this row only
        self.CONTACT_INFO = CONTACT_INFO
        self.SM_INFO = SM_INFO

    # from excel sheet

    # to ensure right data is loading

class Contact (Person):
    def __init__(self, CONTACT_INFO):
        Person.__init__ (self, EMAIL, PHONE, ADDRESS, NOK_NAME, NOK_PHONE, NOK_ADDRESS)
        self.EMAIL = EMAIL
        self.PHONE = PHONE
        self.ADDRESS = ADDRESS
        self.NOK_NAME = NOK_NAME
        self.NOK_PHONE = NOK_PHONE
        self.NOK_ADDRESS = NOK_ADDRESS

class Service_Member (Person):
    def __init__(self, SM_INFO):
        Person.__init__ (self, DODID, BRANCH, STATUS, DESIGNATOR, COC, ETS, BASD, GRADE, SPN)
        self.DODID = DODID
        self.BRANCH = BRANCH
        self.STATUS = STATUS
        self.DESIGNATOR = DESIGNATOR
        self.COC = COC
        self.ETS = ETS
        self.BASD = BASD
        self.GRADE = GRADE


        if ETS < today.strftime("%m/%d/%Y"):
            Veteran = True


class VA_Eligibility (Service_Member):

    def __init__(self, SPN):
        self.SPN = SPN
        if ETS < today.strftime ("%m/%d/%Y"):
            Veteran = False
        else:
            True



