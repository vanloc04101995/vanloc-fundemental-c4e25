import sys
sys.stdout.flush()

for i in range(3):
    for j in range(7):
        print("* ", end='', flush=True)
    print()