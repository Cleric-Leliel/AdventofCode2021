#Advent of Code 2021
#Day 7: CRAB. SUB. MARINES.
# aka, the day the devs all got high 
#v1.0 12/07/21 -- Leliel

#Easy one.


import re
import math

#### Load input ####
FileData = open("day7in.txt")
RawIn = FileData.read().split(",")
    
totfuel = []
#print(len(RawIn), min(RawIn),max(RawIn)))

for x in range(int(min(RawIn)), int(max(RawIn))+1):
    target =x
    fuel =0
    #print("Fuel Calc for Pos "+str(target))
    #move all to position X
    for i in range (0, len(RawIn)):
        delta = abs(int(RawIn[i]) - target)
        fuel = fuel + delta
        #print("fuel used = "+ str(fuel))
        
    totfuel.append(str(fuel))
    #print(totfuel)

print(str(min(totfuel)) +" at position "+str(totfuel.index(min(totfuel))))

    
