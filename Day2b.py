#Advent of Code 2021
#Day 2: Dive! Pt 2
#v1.0 12/02/21 -- Leliel

#anyone else play LOGO on the Apple IIe? just me?
x =0      #horizontal    -10 ------- 0 -----10
z =0      #depth
aim = 0   #aim

with open('day2in.txt') as fn:
    for line in fn:
        line = line.rstrip()
        (direction, val) = line.split(" ")
        #print(direction +"|"+val)
        val = int(val)
        if direction.find("forward") > -1:
            x = x + val
            z = z + aim*val
        elif direction.find("up")> -1:
            #z = z - val
            aim = aim - val
        elif direction.find("down")> -1:
           #z = z + val
            aim = aim + val

print("x = ",x)
print("z = ",z)
print(str(int(x)*int(z)))


