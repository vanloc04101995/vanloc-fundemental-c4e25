# Program that converts Celcius(C) into Fahrenheit (F)
check = "y"
while (check=="y"): 
    temC = float(input("Enter the temperature in Celcius? "))
    temF= temC*1.8 +32
    print(temC,"(C) = ",temF,"(F)")
    check = input("Press 'Y' to continue or 'N' to exit: ")
print("The converts have finished")