#Advent of Code 2021
#Day 1: Sonar Sweep
#v1.0 12-01-2021  -- Leliel

meas = []
count= 0

with open('day1in.txt') as fn:
    for line in fn:
        meas.append(int(line.rstrip()))


for i in range(1, len(meas)):
    if meas[i] > meas[i-1]:
        count = count+1


#print(meas)
print(count)
print (str(len(meas)) + " items in list")
        
