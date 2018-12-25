
check = 'y'
while(check=='y'):
    height_cm = float(input("Your height (cm):"))
    weight = float(input("Your weight (kg):"))
    height_m = height_cm/100
    BMI_cal = weight / ( height_m**2)
    print(BMI_cal)
    if BMI_cal <16:
        print("Severely underweight")
    elif BMI_cal < 18.5:
        print("Underweight")
    elif BMI_cal < 25:
        print("Normal")
    elif BMI_cal <30 :
        print("Overweight")
    else:
        print("obese")
    check = input("Press 'Y' to continue or 'N' to exit")
print("SEE YOU AGAIN")