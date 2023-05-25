
import math

s = int(0)
n = int(0)


while True:
    k = input("\nInput Upper Limit: ")
    if k.isnumeric() is True:    
        for n in range(int(k)):
            s += (((-1)**n)*4)/(2*n+1)
        break
    else:
        print("\nInvalid Input! Type a Number.")
        
print(s)

# k : (Upper Limit)
# n : (Lower Limit)
# s : (const)