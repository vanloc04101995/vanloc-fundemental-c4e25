def sum_to(n) :
  for i in range(0,n+1):
    s += i
  return s
check1 = "y"
sum_ = 0
while(check1=="y") :
  number = int(input("So luong can tinh tong :"))
  sum_ = sum_to(number)
  print("Tong",number,"so la:",sum_)
  check1 = input("Press 'Y' to continue or 'N' to exit: ")
print("SEE YOU AGAIN")