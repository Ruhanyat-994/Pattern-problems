'''printing right sided increasing triangle'''
n = int(input("Enter a number :"))
for i in range(n):

    for j in range(i+1): #for increasing stars
        print(" ",end="")

    for j in range(i,n): #for decreasing spaces
        print("*",end="")

    print()