from random import randint
list_dict = [
    {'1' : 35,'2' : 36,'3' : 40,'4' : 44},
    {'1' : 12,'2' : 13,'3' : 14,'4' : 15},
    {'1' : 29,'2' : 30,'3' : 31,'4' : 32},
]
check_continue = "y"
while check_continue == "y":
        points = 0
        print("if x = 8, then what is the value of  4(x+3)?")
        for i in list_dict[0]:
            print(i,".",list_dict[0][i])
        answer = input("you choose:")
        result = list_dict[0][answer]/4 -3
        if result == 8:
            print("Hura")
            points +=1
        else :
            print("Sorry")
        print("if x = 4, then what is the value of  2(x+3)?")
        for i in list_dict[1]:
            print(i,".",list_dict[1][i])
        answer = input("you choose:")
        result = list_dict[1][answer]/2 -3
        if result == 4:
            print("Hura")
            points += 1
        else :
            print("Sorry")
        if points == 2 :
            print ("You correctly anwser 2 out of 2 questions")
        elif points == 1:
            print ("You correctly anwser 1 out of 2 questions")
        else :
            print ("You correctly anwser 0 out of 2 questions")
        check_continue = input("Continue?(Y or N)")