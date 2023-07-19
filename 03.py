for i in range(5,0,-1):
    print(' ' * i,end=' ')
    for j in range(6-i,0,-1):
        print('*',end="")
    print()


for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

"""
    *
   **
  ***
 ****
*****
"""
