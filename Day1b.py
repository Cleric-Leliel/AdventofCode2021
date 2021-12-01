#Advent of Code 2021
#Day 1: Sonar Sweep pt 2
#v1.0 12-01-2021  -- Leliel

meas = []
count= 0

with open('day1in.txt') as fn:
    for line in fn:
        meas.append(int(line.rstrip()))


for i in range(3, len(meas)):
    sum1 = meas[i-1] + meas[i-2] + meas[i-3]  #0 - 3
    sum2 = meas[i] + meas[i-1] + meas[i-2]    #1 - 4
    if sum2 > sum1:
        count = count+1


#print(meas)
print(count)
print (str(len(meas)) + " items in list")
        
