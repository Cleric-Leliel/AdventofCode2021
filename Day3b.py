#Advent of Code 2021
#Day 3: Binary Diagnostic
#v1.0 12/03/21 -- Leliel
# Note: This could have been a lot shorter if I'd bothered to make a function but w/e.
# Day 3 and I'm already getting sloppy??

from collections import Counter  #Nifty mode, mean, etc for lists


####Load matrix ####
col=[]
i = 0 # row
with open('day3in.txt') as fn:
    for line in fn:
        bits = list(line.rstrip())
        col.append(bits)
        i = i +1
#Initializations
gamma =""     
epsi = ""
O2 = ""
CO2 =""

####Find Gamma and Epsilon ####
for x in range(0,len(col[0])):
    gambits = []
    for y in range(0,len(col)):
        gambits.append(col[y][x])
    gammode = Counter(gambits).most_common(1)[0][0]  #most common, aka mode
    eplcb = Counter(gambits).most_common()[1][0]   #least common
    #print("mode of bit" +str(x) + " is "+ str(gammode))
    #print("lcb  of bit" +str(x) + " is "+ str(eplcb))
    gamma = gamma + str(gammode)
    epsi = epsi + str(eplcb)

print(gamma)          #No one expects Python's extra-nifty string decimal to binary conversion
gamma = int(gamma,2)
print(gamma)

print(epsi)
epsi = int(epsi,2)
print(epsi)

print("Power = "+str(epsi*gamma))

####Find O2 ####
col1 = col[:]   #copy, dont make a reference
for x in range(0,len(col1[0])):
   # print("-- "+str(x)+" --")
    y=0
    O2bits =[]
    for y in range(0,len(col1)):    # Make list to compare to
        O2bits.append(col1[y][x])

    #print(O2bits)
        
    if(len(Counter(O2bits).most_common())== 1):   #if reduced to 1 bit
            y=y  #GNDN
            #print("keep all" + str(col1))
    else:
        mode = Counter(O2bits).most_common(1)[0][0]  #most common, aka mode
        lcb = Counter(O2bits).most_common()[1][0]   #least common
        nmode = Counter(O2bits).most_common(1)[0][1] # # of times most common appears in list
        nlcb =  Counter(O2bits).most_common()[1][1]  # # of times least common appears in list
       # print("most common = "+str(mode) +" in position "+str(x))
        y=0
        while y in range(0,len(col1)):
            if( nmode == nlcb) :             #tie goes to "1"'s
            #    print("tie: mode --> 1")
                mode = 1
            if(str(col1[y][x]).find(str(mode)) >= 0):  #str compare bit to mode bit
           #     print("keep " + str(col1[y]))
                y=y+1
            else:
           #     print("Remove "+str(col1[y]))
                col1.remove(col1[y]) #and do not increment counter


print('-----')    
col1 = col1[0] #un-nest this
print(col1)
for j in col1:  #She turned me into a Newt! I mean a String!
    O2 = O2 + str(j)

print(O2)
O2 = int(O2,2)
print(O2)

####Find CO2 ####
col2 = col[:] #copy, dont make a reference
for x in range(0,len(col2[0])):
    #print("-- "+str(x)+" --")
    y=0
    CO2bits =[]
    for y in range(0,len(col2)):    # Make list to compare to
        CO2bits.append(col2[y][x])
        
    if(len(Counter(CO2bits).most_common())== 1):   #if reduced to 1 bit
            #print("keep all" + str(col2))
            y=y  #GNDN
    else:
        mode = Counter(CO2bits).most_common(1)[0][0]  #most common, aka mode
        lcb = Counter(CO2bits).most_common()[1][0]   #least common
        nmode = Counter(CO2bits).most_common(1)[0][1] # # of times most common appears in list
        nlcb =  Counter(CO2bits).most_common()[1][1]  # # of times least common appears in list
        #print("least common = "+str(lcb) +" in position "+str(x))
        y=0
        while y in range(0,len(col2)):
            if( nmode == nlcb) :             #tie goes to "0"'s
              #  print("tie: lcb --> 0")
                lcb = 0
            if(str(col2[y][x]).find(str(lcb)) >= 0):  #str compare bit to lcb bit
              #  print("keep " + str(col2[y]))
                y=y+1
            else:
              #  print("Remove "+str(col2[y]))
                col2.remove(col2[y]) #and do not increment counter
                
print('-----')    
col2 = col2[0]   #un-nest this
print(col2)
CO2 =""
for j in col2:    #She turned me into a Newt! I mean a String!
    CO2 = CO2 + str(j)

print(CO2)
CO2 = int(CO2,2)
print(CO2)

print("Life support = "+str(CO2*O2))



