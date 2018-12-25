def dayOfWeek(day) :
    return{
    'Sunday' :0,
    'Monday'  :1,
    'Tuesday' :2,
    'wednesday':3,
    'Thursday' :4,
    'Friday :5,
    'Saturday':6,
    }[day]
check1 = "y"
while(check1=="y") :
  number = int(input("Press a number :"))
  dayOfWeek(number)
  check1 = input("Press 'Y' to continue or 'N' to exit: ")
print("SEE YOU AGAIN")