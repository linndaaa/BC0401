#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:58:50 2020

@author: linda
"""


import Lunch

def lunch_menu():
    menu=f"""Lunch Time
    Select option:
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
           
import Dinner

def dinner_menu():
    menuItem = """Dinner Time
    Welcome to Main Page:
        Do input the relevant information.
        1. Check availability 
        2. Make reservation 
        X. End application
        Enter your choice: 
        """
        
    while True:
        choice = input(menuItem)
        if choice == '1':
            Dinner.availability()
        elif choice == '2':
            Dinner.Cust_details()           
        elif choice.upper() == 'X':
            
            break


def main():
    menu = """Please select Lunch or Dinner
    1. Lunch
    2. Dinner
    0. Back to Main Page"""
      
    while True:
        choice = int(input(menu))
        if choice == 1:
            lunch_menu()
        elif choice == 2:
            dinner_menu()
        elif choice == 0: 
            break
        else:
            print("please input 1 or 2 only!")
            

