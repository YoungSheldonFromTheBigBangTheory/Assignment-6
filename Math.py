import math

s = int(0)
n = int(0)
k = int(input("Input Upper Limit: "))

for n in range(k):
    s += (((-1)**n)*4)/(2*n+1)

print(s)

# first : is the first value of (n) (the index of summation)
# last : is the last value of (n)
# const : is the number that you want to sum its multiplication each (n) times with (n)