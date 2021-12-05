#Advent of Code 2021
#Day 4: Giant Squid BINGO
#v1.0 12/04/21 -- Leliel

import re

#THE PLAN:
#1. DEFINE WINSETS
#2. FIND WINSETS IN CHIPORDER SET
#### LOWEST INDEX WINS


class Card:
##    # Class attribute
    def __init__(self, ID, winsets):
        self.ID = ID
        self.winsets = winsets
    # Replace .description() with __str__()
    def __str__(self):
        return f"CARD {self.ID} : {self.winsets}"

#### Load matrix ####
FileData = open("day4in.txt")
RawIn = FileData.read().splitlines()   #Look Ma, no newlines!
    
chiporder = RawIn[0].split(",")

TotNumCards = int((len(RawIn) -1) /6)
print("Expected # of cards : " + str(TotNumCards))

allcards = dict()
### MAKE CARDS ### 
offset=2
for ID in range(1,TotNumCards+1):    
    card1=[]
    c1winsets=[]
    for i in range(0,5): 
        row = RawIn[offset+i].split()
        card1.append(row)
        c1winsets.append(row)
        
    for x in range(0,5):
        cols = []
        for y in range(0,5):
            cols.append(card1[y][x])
        c1winsets.append(cols)
        #print(cols)
    offset = offset + 6   #go to next card    
    mycard = Card(str(ID),c1winsets)
    allcards[ID] = mycard

### When do I BINGO? ###
winningcall = len(chiporder)+1
winner= 0
for ID in range(1,TotNumCards+1):
    thiscard = allcards[ID]
    #print(thiscard)

    cardmin = len(chiporder)+1         
    for j in range(0,len(thiscard.winsets)):     #check each winset
        if(set(c1winsets[j]) <= set(chiporder)):     #a <= b means "a is a subset of b
            winsetmax = 0  
            for k in range(0,len(thiscard.winsets[0])):
                bingo= chiporder.index(thiscard.winsets[j][k])
               # print(str(c1winsets[j][k]) +" called at index " + str(bingo))
                winsetmax = max(winsetmax, bingo)
            #print("Card "+ str(ID) +" wins with winset "+str(j)+" at "+str(winsetmax))
            cardmin = min(cardmin,winsetmax)
        else:
            print("Card "+ str(ID) +" cannot BINGO with winset "+str(j)+"!")

    print("Card "+ str(ID) +" wins at index "+ str(cardmin))
    if(cardmin<winningcall):
        winningcall = cardmin
        winner = ID

print("Card " +str(winner) +" is the winner with "+str(chiporder[winningcall]) +" at call index "+str(winningcall))

print(allcards[winner])

AllCalled = chiporder[0:winningcall+1]
print("All called")
print(AllCalled)

WinningCard = set()
for s in allcards[winner].winsets:
    WinningCard.update(set(s))   #no duplicates
#print(WinningCard)

Uncovered = WinningCard - set(AllCalled)
print("Uncovered Numbers on winning card")
print(Uncovered)

Sum =0
for num in Uncovered:
    Sum = Sum +int(num)

print(Sum)

Final = chiporder[winningcall]
print(Final)

Product = int(Sum) * int(Final)
print(Product)


