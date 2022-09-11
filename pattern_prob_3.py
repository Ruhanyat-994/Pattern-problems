n = int(input('''Enter a number 
for printing a pattern of decreasing triangle: '''))
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()