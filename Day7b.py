#Advent of Code 2021
#Day 7: CRAB. SUB. MARINES.
# aka, the day the devs all got high 
#v1.0 12/07/21 -- Leliel
#v2.0 12/07/21 -- Leliel Part II

#Pretty sure this whole thing could be skipped with
#math, but coded it out anyway.
#Runs too slow on full puzzle input

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
    sumfuel=0
    #print("Fuel Calc for Pos "+str(target))
    #move all to position X
    for i in range (0, len(RawIn)):
        delta = abs(int(RawIn[i]) - target)
        stepcost =0
        for c in range(1,delta+1):
            stepcost = stepcost + 1 
            fuel = fuel + stepcost
            #print ("From "+str(RawIn[i])+" Step "+str(c)+ "costs "+ str(stepcost)+ "  tot for pos "+str(target)+" = "+str(fuel))
        #print("fuel used = "+ str(fuel))
        sumfuel = sumfuel + fuel
        fuel =0
        
    totfuel.append(str(sumfuel))
    #print(totfuel)

print(str(min(totfuel)) +" at position "+str(totfuel.index(min(totfuel))))

    
