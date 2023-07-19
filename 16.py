f = l = 5
for i in range(1,6):
    for j in range(1,10):
        if j == f or j == l :
            print("* ",end="")
        else:
            print("  ",end="")
    f+=1
    l-=1
    print()
f = 2 ; l = 8
for i in range(1,5):
    for j in range(1,10):
        if j == f or j == l :
            print('* ',end="")
        else:
            print('  ',end="")
    f+=1
    l-=1
    print()

