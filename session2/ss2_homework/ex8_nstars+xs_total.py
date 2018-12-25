import sys
sys.stdout.flush()

n = int(input("Press the number of stars:"))
a = int((n/2)+1)
print()
for i in range(a):
  print("x ", end='', flush=True)
  if i!=(a-1):
    print("* ", end='', flush=True)
  else:
    print("") 