#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:08:35 2020

@author: linda
"""

# the main stuff, to get customer details 
def Cust_details():
    global details  
    details = []
    
    cust_details= """What slot is the customers reserving?     
    1: 6pm - 8pm 
    2: 8.30pm-10.30pm
    Enter your choice:
    """
    
    get_days()
    while True:
        try:
            choice = int(input(cust_details))
            if choice == 1:
                while True:
                    c = input("Enter customer phone number")
                    if len(str(c)) == 8:
                     n =input("Enter customer name")
                     details.append([n,c])
                     createfile1()
                     break
                else:
                    print("wrong no. of digits")                   
            elif choice == 2:
                 while True:
                    c = int(input("Enter customer phone number"))
                    if len(str(c)) == 8:
                        n=input("Enter customer name")
                        details.append([n,c])
                        createfile2()
                        break
                    else:
                        print("Invalid number")
            else: 
                print("Choose 1 or 2 only")
            break
        except ValueError:
            print("Number only")




# to create csv for slot 1
def createfile1(): 
    from datetime import datetime, timedelta 
    file=datetime.now() 
    filename = file + timedelta(days= day_from_now)  
    import pandas as pd
    import os 
    outfile = open(filename.strftime("%d %B %Y")+"1"+".csv", 'a+')
    filesize = os.stat(filename.strftime("%d %B %Y")+"1"+".csv").st_size
    if filesize == 0:
        df=pd.DataFrame(details, columns = ["Customer Name ", "Phone no."])
        df.to_csv(outfile, index=False)      
    else:
        df=pd.DataFrame(details)
        df.to_csv(outfile, index = False, header = False)
        outfile.close()

#to create csv for slot 2 
def createfile2(): 
    from datetime import datetime, timedelta 
    file=datetime.now() 
    filename = file + timedelta(days= day_from_now)  
    import pandas as pd
    import os 
    outfile = open(filename.strftime("%d %B %Y")+"2"+".csv", 'a+')
    filesize = os.stat(filename.strftime("%d %B %Y")+"2"+".csv").st_size
    if filesize == 0:
        df=pd.DataFrame(details, columns = ["Customer Name ", "Phone no."])
        df.to_csv(outfile, index=False)      
    else:
        df=pd.DataFrame(details)
        df.to_csv(outfile, index = False, header = False)
        outfile.close()







#this is the definition for the no. of days they want to make reservation from today
# so customer can book for today till 7 days later
def get_days():
    global day_from_now
    while True:
        try:
            day_from_now=int(input("How many days from TODAY? "))
            
            if day_from_now >7 or day_from_now < 0:
                print("Please choose 1-7 days only")
            else:
                print("Chosen days:",day_from_now)
                break
            
        except ValueError:
            print("Please choose numeric number!")




def availability():
    day_from_now=int(input("How many days from TODAY? "))
    from datetime import datetime, timedelta 
    file=datetime.now() 
    filename = file + timedelta(days= day_from_now)  
    if FileNotFoundError:
        print("No reservations as of now for this date!")
    else:
        import csv
        file = open(filename.strftime("%d %B %Y")+"1"+".csv", 'r')
        reader = csv.reader(file)
        num_cust1= (len(list(reader))/2) -1
        print (f"There are {num_cust1} in slot 1(6.30PM - 8.30pm)")
        file = open(filename.strftime("%d %B %Y")+"2"+".csv", 'r')
        reader = csv.reader(file)
        num_cust2= (len(list(reader))/2) -1
        print (f"There are {num_cust2} in slot 2")
        if FileNotFoundError:
            print("No reservations as of now for this date!")
            
        
        
   







