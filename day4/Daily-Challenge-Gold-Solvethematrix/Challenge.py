MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Convert the string into a 2D list (matrix)
lines = [list(line) for line in MATRIX_STR.strip().split('\n')]
rows = len(lines)
cols = len(lines[0])

# Step 2: Read the matrix column-wise (top to bottom)
col_text = ""
for c in range(cols):
    for r in range(rows):
        col_text += lines[r][c]

# Step 3: Replace non-alphabetic groups with a single space
decoded = ""
add_space = False  # flag to control space insertion
for ch in col_text:
    if ch.isalpha():
        # if we just came out of a symbol sequence, add a space first
        if add_space and decoded and decoded[-1] != ' ':
            decoded += ' '
        decoded += ch
        add_space = False
    else:
        # mark that we’ve hit a non-alpha group
        add_space = True
# Step 4: Clean up any extra spaces
decoded = decoded.strip()

# Step 5: Print the hidden message
print(decoded)
