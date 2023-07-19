k=1
for i in range(1,5):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

for i in range(6,0,-1):
    print(' ' * (6-i) + '*' * i )