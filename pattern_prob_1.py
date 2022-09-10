'''same coloumn and same row star problem like 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * '''
n = int (input("Enter your number :"))
for i in range(n):
    for j in range(n):
        print(" * ",end="")
    print()