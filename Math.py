import math

x = 1
h = int(input(": "))

#for i in range(h):
    #pi = (4/x)

#print(pi)



def sigma(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum