'''printing a reverese hill pattern'''
n=int(input("Enter the number you like :"))
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):#for decreasing a coloumn
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print() 