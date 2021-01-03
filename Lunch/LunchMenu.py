# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:31:49 2020

@author: flore
"""


import Lunch

def lunchmenu():
    menu=f"""Select option:
        1. Wait time
        2. Customer leave
        3. No Queue - Update Data
        X. Exit Application
        OPTION: """
  
    while True:
        period = input(menu)
        if period == "1":
            Lunch.queue()
        elif period == "2":
            Lunch.cust_out_restaurant()
        elif period == "3":
            Lunch.diff_out() #when no customer in queue, update the data
            Lunch.avg_diff()  
            Lunch.no_queue() #delete existing data on customer leaving interval
        elif period.upper() == 'X':
            break
           
lunchmenu()

#lunch.no_queue() executed when no queue e.g no queue but queue begins again 1hr later
#inaccurate wait time if diff of 1 hr is added to lunch.diff_out()

#only want the difference of customer leaving when there is a queue