# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:01:04 2020

@author: Main
"""

import math
defMin,mini,tries,defMax,maxi,finish,defAvg,Avg,isFirstInput=0,0,0,100,100,False,50,50,True 
while (finish == False):     
        if(isFirstInput == True): 
            userName = input("Hi, what is your name?")
            print("Hello "+ userName + "! Let's play a game!\nThink of a random number from 1 to 100, and i'll try to guess it!")
            isFirstInput =False  
        tries+=1
        getAck = input("Is it " + str(Avg) + "? (yes/no)")
        if(getAck == "yes"):
           getAck = input("Yeey! i got it in "+ str(tries) + " tries!\nDo you want to play more?")
           if(getAck == "yes"):
                mini,tries,maxi,Avg,isFirstInput=defMin,0,defMax,defAvg,True   
           else:
                finish = True
                print("Bye-bye")            
        elif(getAck == "no"):            
            getAck = input("Is the number larger than " + str(Avg) + "? (yes/no)")
            if(getAck == "yes"): 
                mini = Avg                
                if(Avg >= defAvg):  Avg= math.ceil((mini + maxi) / 2) if maxi == defMax else math.floor((mini + maxi) / 2)
                else: Avg= math.floor((maxi + mini) / 2) if maxi == defMax else math.ceil((mini + maxi) / 2)
            elif(getAck == "no"):
                maxi = Avg
                if (Avg <= defAvg): Avg = math.ceil((maxi - mini) / 2) if mini == defMin else math.ceil((maxi + mini) / 2)
                else: Avg = math.floor((maxi + mini) / 2)