from datetime import datetime as dt
from datetime import timedelta
from time import sleep
import pygame


# pygame initiation
pygame.init()
pygame.mixer.init()
#add custom sounds
sound = pygame.mixer.Sound("bell.ogg")


def main():

    print("\n\n(pygame does the sound, thanks pygame, anyway LADIES AND GENTLEMEN, WELCOME TO THE STAGE...\n\n\n")
    print("ooooooo________oooo______oo_________ooooooo_____oooooooo_")
    print("oo____oo_____oo____oo____oo_________oo____oo_______oo____")
    print("oooooooo____oo___________oo_________oo____oo_______oo____")
    print("oo____oo____oo___________oo_________oooooo_________oo____")
    print("oo____oo_____oo____oo____oo_________oo_____________oo____")
    print("ooooooo________oooo______ooooooo____oo_____________oo____")
    print("_________________________________________________________")
    print("\nbardoctorus_command_line_pomodoro_timer\n\n")

    p = input("Press enter for standard 25 minute Pomodoropolous with 5 \
minute breaks.\nAlternatively enter your chosen pomolomanomanom time in minutes\n")
    if (p == ""):
        d = 25
        f = 5   
    else:
        try:
            d = int(p)       
            f = int(input("Enter break time in mins\n"))
        except ValueError:
            raise SystemExit("TypeError: Did you enter something that isn't a number?")  
    g = [d,f,d,f,d,f,d]
    sound.play()
    print("\nGetting a Pom On in "+str(g[0])+\
        " minute intervals with "+str(g[1])+" minute breaks\n\
Press Ctrl + C to quit at any time.\n\nGo!\n")
    pom_phase = 1
    print("Pomgrominate Phase: "+str(pom_phase)+"/4")
    for q, i in enumerate(g):
        
        
        
        start_time = dt.now()

        end_time = start_time + timedelta (seconds = i) # ! seconds version for testing Change to mins
        timer (end_time)
        if q == 6:
            break
        elif q % 2 == 0:
            print("\n\n|---  Breaktime!   ---|\n")
        else:
            print("\n\n|--- Back to work! ---|\n")
            pom_phase += 1
            print("Pomgrominate Phase: "+str(pom_phase)+"/4\n")



    print("\n\n\nYou have completed 4 pomeranians. Have a 15-20 minute break then start me again!\n")

def timer(end_time):   
    while True:        
        current_time = dt.now()
        if(current_time >= end_time):         
            sound.play()
            sleep(2)
            return False
        else:      
            print("Current Time: "+str(current_time)[11:-7]+"|-----|End time for this phase: "+str(end_time)[11:-7], end="\r")         
            sleep(0.25)

if __name__ == "__main__":  
    main()


