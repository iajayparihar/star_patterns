# k = 0
# n=7 # use only odd numbers for triangle 
# for i in range(1,n):
#     print("  " * (i-1) + '* ' * (n - k))
#     k+=2


n=3
for i in range(n, 0, -1):
    print('  ' * (n - i) + '* ' * (2 * i - 1))

