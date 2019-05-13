from datetime import datetime as dt
from datetime import timedelta
from time import sleep
import winsound
import os


start_time = dt.now()

end_time = start_time + timedelta (seconds = 2)

current_time = dt.now()

while running:
    current_time = dt.now()

    if(current_time >= end_time):
        winsound.PlaySound("ting.wav", winsound.SND_ASYNC)
        print("Done!")
        sleep(5)
        
        running = False
    else:
        print("Current Time :"+str(current_time))
        print("End Time: "+str(end_time))
        sleep(0.25)

print("Thank fuck that is over")