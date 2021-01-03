# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:08:11 2020

@author: flore
"""
#%%
queuecount = 0

                
def queue():
    global queuecount, period
    while True:
        try:
            new_cust=int(input(f"""Choose option:
1. New customer joining queue
2. Customer leaving queue 
Option: """)) #customer leave queue before entering restaurant
            if new_cust == 1:
                queuecount += 1
                break
            elif new_cust == 2:  
                queuecount -= 1
                break
            else:
              print("Please choose 1/2")
              
        except ValueError:
           print("Please choose 1/2")     
              
        
    import pandas as pd

        
    df=pd.read_csv("pythonavg.csv")
    wait_time = df["avg"][0] # assume restaurant open for 4 hours
    
    if queuecount <= 5:
        
        for i in range(1,queuecount+1):
            wait= wait_time*i
            waiting = 5*round(wait/5) #round the waiting time to the nearest multiple of 5
        print(f'Wait time is {waiting} mins')
    if queuecount >5:
        for i in range(1,queuecount+1):
            wait= wait_time*i
            waiting = 5*round(wait/5)


        while True:            
            try:
                takeaway_choice=input(f"We have exceeded number of people allowed in the queue,\nwould customer like to takeaway instead? \n[y/n]")
                if takeaway_choice.lower() == "y":
                    queuecount -= 1
                    break 
                elif takeaway_choice.lower() == "n":
                    print(f'''Let customer know they have to come back later in around {waiting} mins''') #max number of grps in the queue exceeded
                    break #ask customer to return later
            
                else:
                    print("Please choose y/n")
            
            except ValueError:
               print("Please choose y/n")
               
               
               
#%%
def cust_out_restaurant(): #cust leave restaurant after dining
    import pandas as pd
    import os 
    from datetime import datetime
    time_now=[]
    time=datetime.now().strftime('%H:%M:%S')  
    time_now.append(time)
    
    outfile = open("pythonout.csv", 'a+')
    filesize = os.stat("pythonout.csv").st_size
    if filesize == 0:
        df=pd.DataFrame( time_now, columns = ["Time"])
        df.to_csv(outfile, index=False)      
    else:
        df=pd.DataFrame(time_now)
        df.to_csv(outfile, index = False, header = False)
        outfile.close()
   
#%%     
def no_queue():
    import os
    os.remove('pythonout.csv') #delete file to only take in time diff btw customer leaving, excluding when queue empty
    
#%%

def diff_out():  #time diff of customers leaving 
    time=[]
    diff= []
    import pandas as pd            
    df=pd.read_csv("pythonout.csv")
    for i in df.index: 
         time.append(df["Time"][i])

    from datetime import datetime
    for x in range(1,len(time)):
        FMT = '%H:%M:%S'
        d= datetime.strptime(time[x], FMT) - datetime.strptime(time[x-1], FMT)
        d =d.total_seconds()/60
        diff.append(d)   
        
    import os 
    outfile = open("pythondiff.csv", 'a+') #keep past data of time diff for more accurate value
    filesize = os.stat("pythondiff.csv").st_size
    if filesize == 0:
        df=pd.DataFrame(diff, columns = ["Diff"])
        df.to_csv(outfile, index=False)      
    else:
        df=pd.DataFrame(diff)
        df.to_csv(outfile, index = False, header = False)
        outfile.close()

#%%
def avg_diff(): #avg time diff of customers leaving 
    import pandas as pd 
    list1=[]
    avg_data = {"avg":list1}
    df=pd.read_csv("pythondiff.csv")
    avg = df.Diff.mean()
    list1.append(avg)
    
    
    import os 
     
    outfile = open("pythonavg.csv", 'w+') #w+ to change avg time everytime data is updated
    filesize = os.stat("pythonavg.csv").st_size
    if filesize == 0:
        df=pd.DataFrame(avg_data)
        df.to_csv(outfile, index=False)      
    else:
        df=pd.DataFrame(avg_data)
        df.to_csv(outfile, index = False, header = False)
        outfile.close()


    










