#Advent of Code 2021
#Day 3: Binary Diagnostic
#v1.0 12/03/21 -- Leliel

from collections import Counter  #Nifty mode, mean, etc for lists

#Initializations
gamma =""     
epsi = ""    
i = 0 # row
col=[]
gambits =[]


####Load matrix ####
with open('day3in.txt') as fn:
    for line in fn:
        bits = list(line.rstrip())
        col.append(bits)
        i = i +1

#print(col[0])
#print(len(col[0]))
#print(len(col))

####Find Gamma and Epsilon ####
for x in range(0,len(col[0])):
    gambits = []
    for y in range(0,len(col)):
        gambits.append(col[y][x])
    gammode = Counter(gambits).most_common(1)[0][0]   #most common, aka mode
    eplcb = Counter(gambits).most_common()[1][0]   #least common
    #print(Counter(gambits).most_common())
    print("mode of bit" +str(x) + " is "+ str(gammode))
    print("lcb  of bit" +str(x) + " is "+ str(eplcb))
    gamma = gamma + str(gammode)
    epsi = epsi + str(eplcb)

print(gamma)          #No one expects Python's extra-nifty string decimal to binary conversion
gamma = int(gamma,2)
print(gamma)

print(epsi)
epsi = int(epsi,2)
print(epsi)


print("Power = "+str(epsi*gamma))
