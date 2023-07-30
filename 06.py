n = 5  # Number of rows

# Upper half of the diamond
for i in range(n):
    print(' ' * (n - i) + '*' * (2 * i + 1))

# Lower half of the diamond
for i in range(n-2, -1, -1):
    print(' ' * (n - i) + '*' * (2 * i + 1))
