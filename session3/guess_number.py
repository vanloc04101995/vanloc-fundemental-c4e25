from random import randint

a = randint(1, 100)
print(a)
loop = True
while loop:
    guess = int(input("Enter your number:"))
    loop = False 
    if a != guess:
       print("Sorry!")
       guess = int(input("enter your number again:"))
       loop = True
    
print("BINGO")
