
for i in range(1, 5):
    print(" " * (5 - i),end=' ')
    num = i
    for j in range(i):
        print(num,end="")
        num +=1
    num -= 2
    for k in range(i-1):
        print(num,end="")
        num -= 1
    print()
    num+=1