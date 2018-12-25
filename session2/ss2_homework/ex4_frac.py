def factorial(n):
   if n == 1:
       return 1
   else:
       return n*factorial(n-1)

# Change this value for a different result
num = int(input("Press a number:"))

# check is the number is negative
print("Sorry!") if num < 0 else print("The factorial of 0 is 1") if num ==0 else print("The factorial of",num,"is",factorial(num)) 

   