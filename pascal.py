from math import factorial

n = int(input("Pascal triangle for how many rows?:"))

#main for loop

for i in range(n+1):
    #loop for left spacing
    for j in range(n-i+1):
        print(end=" ")
    #foroop for printing number values
    for k in range(i+1):
        ele = factorial(i)/(factorial(k)*factorial(i-k))
        print(int(ele),end=" ")
    #new line
    print()
