#Advent of Code 2021
#Day 8: Old Alarm Clock Displays
#v1.0 12/08/21 -- Leliel

#### Load  data ####
FileData = open("day8in.txt")
RawIn = FileData.read().splitlines()   

Total = 0
for j in range(0,len(RawIn)):
    Signal = RawIn[j].split(" | ")
    Signal = Signal[1].split(" ")
    #print(Signal)
    count = 0
    for i in range(0,len(Signal)):
        if(len(Signal[i]) == 2):
           One = Signal[i]
           count = count +1
        elif(len(Signal[i]) == 4):
           Four = Signal[i]
           count = count +1
        elif(len(Signal[i]) == 3):
           Seven = Signal[i]
           count = count +1)
        elif(len(Signal[i]) == 7):
           Eight = Signal[i]
           count = count + 1
           
    Total = Total+count

# Zero - 6 lights
# Two - 5 lights
# Three - 5 lights
# Five - 5 lights
# Six - 6 lights
# Nine - 6 lights
         

print(Total)
