#Program that calculates the area of a circle
import math
check = "y"
while (check=="y"): 
    r = int(input("Radius ? "))
    area = r**2*math.pi
    print("Area = ",area)
    check = input("Press 'Y' to continue or 'N' to exit: ")
print("The calculations have finished")