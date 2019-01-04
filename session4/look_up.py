abbrve = ["btw","afk", "lol","YOLO","wth","WHO","WTO"]

abbreviation = {
    "btw" : "By the way", 
    "afk" : "Away from keyborad",
    "lol" : "Laugh our loud",
    "YOLO" : "You only live one",
    "wth" : "What the hell?",
    "WHO" : "World Health Organization",
    "WTO" : "World Trade Organization"
}
while True:
    abbr = input("Enter code:")
    if abbr not in abbreviation:
        print("This code does not exist")
        check_update = input("Do you want to create this one:")
        abbr_create = input("Enter translation:")
        abbreviation[abbr] = abbr_create
    else :
        print(abbreviation[abbr])
        check = input("Do you want to update(Y or N)?")
        if check =="y" or check =="Y":
            abbr_update = input("Enter the translation you want to update:")
            abbreviation[abbr] = abbr_update
            print(abbreviation)
            check = input("Do you want to update(Y or N)?")