n=69
for i in range(5,0,-1):
    for j in range(n,n-i,-1):
        print(chr(j),end=' ')
    print()