# x is a first printing point and 
# y is a second printing point

x=y=n=6 
for i in range(1,n):
    for j in range(1,2*n):
        if  j == x or j == y :
            print("*",end="")
        else:
            print(" ",end="")
    x+=1
    y-=1
    print()
print('* ' * 6)