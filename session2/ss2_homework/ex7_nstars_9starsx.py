import sys
sys.stdout.flush()

n = int(input("Press the number of stars:"))
for i in range(n):
 print("* ", end='', flush=True)

print()
for i in range(5):
  print("x ", end='', flush=True)
  if i!=4:
    print("* ", end='', flush=True)
  else:
    print("")  