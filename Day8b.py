#Advent of Code 2021
#Day 8: Old Alarm Clock Displays 
#v1.0 12/08/21 -- Leliel
#v2.0 12/08/21 -- Leliel Part II

#initializations
Zero, One, Two, Three, Four = set(),set(),set(),set(),set()
Five, Six, Seven, Eight, Nine = set(),set(),set(),set(),set()
lights5, lights6 = [], []
BD = set()
Total = 0


#### Load  data ####
FileData = open("day8in.txt")
RawIn = FileData.read().splitlines()   #Look Ma, no newlines!


###Define Number Display Codes from Signal Data ###
Total = 0
for j in range(0,len(RawIn)):   #Each Row is a display set
    Line = RawIn[j].split(" | ")
    Signal = Line[0].split(" ")
    Output = Line[1].split(" ")
    outcode = ""
    for i in range(0,len(Signal)):      # GET 1, 4 ,7 ,8
        if(len(str(Signal[i])) == 2):
           One = set(Signal[i])
        elif(len(Signal[i]) == 4):
           Four = set(Signal[i])
        elif(len(Signal[i]) == 3):
           Seven = set(Signal[i])       # If didn't want to check for invalid input, could drop defining 
        elif(len(Signal[i]) == 7):      #  sets for 7 and 8 as they aren't used again.
           Eight = set(Signal[i])
        elif(len(Signal[i]) == 5):
            lights5.append(set(Signal[i]))
        elif(len(Signal[i]) == 6):
            lights6.append(set(Signal[i]))
        else:
            print("invalid signal found")
    
    BD = Four - One   #intermediate for set compares
    k=0
    while (len(lights5)> 0):         # GET 2, 3, 5 
        if (One <= lights5[k]):      #a <= b means "a is a subset of b
            Three = lights5.pop(k)
        elif (BD <= lights5[k]):
            Five = lights5.pop(k)
        else:
            Two = lights5.pop(k)  #remaining
    

    while (len(lights6)> 0):          # GET 0, 6, 9 
        if not (One <= lights6[k]):   #a <= b means "a is a subset of b
            Six = lights6.pop(k)
        elif not (Four <= lights6[k]): 
            Zero = lights6.pop(k)     #0 contains 1, does not contain 4
        else:
            Nine = lights6.pop(k)  #remaining
            
    #print("Zero, One, Two, Three, Four,Five, Six, Seven, Eight, Nine")    
    #print(Zero, One, Two, Three, Four,Five, Six, Seven, Eight, Nine)

   ###Decipher Output Codes ###
    for i in range(0,len(Output)):
        if(len(str(Output[i])) == 2):
           outcode = outcode + str("1")  #length check assumed quicker than set compare?
        elif(len(Output[i]) == 4):
           Four = set(Output[i])
           outcode = outcode + str("4")
        elif(len(Output[i]) == 3):
           Seven = set(Output[i])
           outcode = outcode + str("7")
        elif(len(Output[i]) == 7):
           outcode = outcode + str("8")
        elif (set(Output[i])<= Zero ) :  # Check IN ORDER to avoid subsets
           outcode = outcode + str("0")
        elif (set(Output[i])<= Five ) :
           outcode = outcode + str("5") 
        elif (set(Output[i])<= Six ) :
           outcode = outcode + str("6")
        elif (set(Output[i])<= Three ) :  
           outcode = outcode + str("3")
        elif (set(Output[i])<= Nine ) :
           outcode = outcode + str("9")
        elif (set(Output[i])<= Two ) :
           outcode = outcode + str("2")
  
    print("Output code = " + outcode)
        
        
    Total = Total +int(outcode)

print("Total ="+ str(Total))

