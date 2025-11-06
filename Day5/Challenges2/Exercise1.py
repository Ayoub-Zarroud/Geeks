# Pattern 1
rows = 3
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
# Pattern 2

rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)
    
# Pattern 3
rows = 5
# Upper half
for i in range(1, rows + 1):
    print('*' * i)
# Lower half
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * i)
