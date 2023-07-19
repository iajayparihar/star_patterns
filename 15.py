f = 1 ; l = 5
for i in range(1,6):
    for j in range(1,10):
        if (i == 1 and j < 6) or (i == 5 and j > 4) or j == f or j == l :
            print('* ',end="")
        else:
            print('  ',end="")
    f+=1;l+=1
    print()