n = int(input('''Enter a number 
for printing a pattern of increasing triangle: '''))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()