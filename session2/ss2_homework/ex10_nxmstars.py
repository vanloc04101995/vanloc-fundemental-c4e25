import sys
sys.stdout.flush()

col = int(input("Column: "))
row = int(input("Row:"))
for i in range(row):
    for j in range(col):
        print("* ", end='', flush=True)
    print()
