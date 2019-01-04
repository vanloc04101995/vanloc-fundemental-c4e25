from random import randint
list_dict = [
    {'1' : 35,'2' : 36,'3' : 40,'4' : 44},
    {'1' : 12,'2' : 13,'3' : 14,'4' : 15},
    {'1' : 29,'2' : 30,'3' : 31,'4' : 32},
]
check_continue = "y"
while check_continue == "y":
    ran_number = randint(0,3)    
    check = True
    while check:
        if ran_number == 0:
            print("if x = 8, then what is the value of  4(x+3)?")
            for i in list_dict[0]:
                print(i,".",list_dict[0][i])
            answer = input("you choose:")
            result = list_dict[0][answer]/4 -3
            if result == 8:
                print("Hura")
                check = False
            else :
                print("Sorry")
                check = True
        elif ran_number == 1:
            print("if x = 4, then what is the value of  2(x+3)?")
            for i in list_dict[1]:
                print(i,".",list_dict[1][i])
            answer = input("you choose:")
            result = list_dict[1][answer]/2 -3
            if result == 4:
                print("Hura")
                check = False
            else :
                print("Sorry")
                check = True
        else:
            print("if x = 2, then what is the value of  5(x+4)?")
            for i in list_dict[2]:
                print(i,".",list_dict[2][i])
            answer = input("you choose:")
            result = list_dict[2][answer]/5 -4
            if result == 2:
                print("Hura")
                check = False
            else :
                print("Sorry")
                check = True
    check_continue = input("Continue?(Y or N)")