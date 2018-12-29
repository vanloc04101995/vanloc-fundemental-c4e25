yob_str = input("Your date of birth:")
while not yob_str.isdigit() :
   print("Not a number")
   yob_str = input("Enter your date of birth again:")
yob = int(yob_str)
while yob < 0 or yob >2018:
   yob_str = input("Enter your date of birth again:")
   yob = int(yob_str)
age = 2018 -yob
print(age)

