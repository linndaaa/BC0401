#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:00:08 2020

@author: linda
"""
import Dinner

def menu():
    menuItem = """Welcome to Main Page:
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

menu()

