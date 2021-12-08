#Advent of Code 2021
#Day 6: Lanternfish
#v1.0 12/06/21 -- Leliel   Part I solution

#Cannot exceed ~128 days

import re
from collections import Counter

i =0
#### Load matrix ####
FileData = open("day6ex.txt")
myfish = FileData.read().split(",")


ENDOFDAYS =  80  #   OMINOUS

for d in range(0,ENDOFDAYS):  
    #print("# of fish on day "+str(d) +"  : "+ str(len(myfish)))
    k=0
    #print(myfish)
    while k <  len(myfish):
        if int(myfish[k]) == 0:
            #print("Day "+str(d)+" Verra Preggo Fisho "+str(f)+" pops!")
            myfish[k] = '6'         #reset this fish
            myfish.append('9')   #make new fish
        else:
            myfish[k] = str(int(myfish[k]) -1)
        k = k +1
    

#print(myfish)
print("# of fish after  "+str(d+1) +" days : "+ str(len(myfish)))







    
