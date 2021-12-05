#Advent of Code 2021
#Day 4: Hydrothermal Venture Bros
#v1.0 12/05/21 -- Leliel

import re
from collections import Counter

#THE PLAN:
#1.DEFINE LINES
#2. IDENTIFY COVERED PTS
#3 COUNT HOW MANY TIMES A PT IS COVERED
   # a = Counter(MyList)


#### Load matrix ####
FileData = open("day5in.txt")
RawIn = FileData.readlines()#.splitlines()   #Look Ma, no newlines!

Covered = []
for line in range(0, len(RawIn)):
    Coords = re.findall(r"\d+", RawIn[line])
    X1 = int(Coords[0])
    Y1 = int(Coords[1])
    X2 = int(Coords[2])
    Y2 = int(Coords[3])

    
    if(X1 == X2):   #Vertical Lines
        Ys = min(Y1,Y2)   #handle backwards lines
        Ye = max(Y1,Y2)
        for i in range(0, (Ye-Ys)+1):
            Covered.append(str(X1)+","+str(Ys+i))   #flip it, flip it back


    if(Y1 == Y2):   #Horizontal Lines
        Xs = min(X1,X2)   #handle backwards lines
        Xe = max(X1,X2)
        for i in range(0, (Xe -Xs)+1):
            Covered.append(str(Xs+i)+","+str(Y1))   #flip it, flip it back

print (Counter(Covered))


dangerzones = list(Counter(Covered).values())   #Let's get DANGEROUS

cnt =0
for v in  dangerzones:
    if v >=2:
        cnt = cnt+1

print(cnt)  
        


