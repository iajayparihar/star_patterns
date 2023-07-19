for i in range(1, 6):
    print(' ' * (5-i) , end='')
    for j in range(i, 0, -1):
        print(j, end='')
    for k in range(2, i + 1):
        print(k, end='')
    print()
