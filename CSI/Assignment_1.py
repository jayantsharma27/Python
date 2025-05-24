n = int(input('Enter the number of rows: '))

print('\nLower Triangle of Stars:\n')
for row in range(n):
    for column in range(row+1):
        print('*', end=' ')
    print()

print('\nUpper Triangle of Stars:\n')
for row in range(n):
    for space in range(row):
        print(' ', end=' ')
    for column in range(n-row):
        print('*',end=' ')
    print()

print('\nPyramid of Stars:\n')
for row in range(n):
    for space in range(n-row-1):
        print(' ',end=' ')
    for column in range(2*row+1):
        print('*', end=' ')
    print()