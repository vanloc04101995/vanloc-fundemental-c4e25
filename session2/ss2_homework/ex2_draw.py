from turtle import *
shape("turtle")
step = 0
k = 3
speed(0)
for i in range(3):
  color('blue') if i == 0 else color('red')    
  for j in range(k):
    fd(100)
    lt(120-step)
  if i == 2:
      fd(100)
      lt(60)
      for j in range(5):
        fd(100)
        color('blue')
        lt(72)
  else:
      k +=1
  step +=30
mainloop()