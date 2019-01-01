import random
# create a sequence of words to choose from
WORDS = ("champion", "meticulous", "hexagon", "difficult")
print(" Welcome to Word Jumble!")
play=input("Do you want to play? (Y or N)")
while play=="y" or play=="Y":
    # a random word
    word = random.choice(WORDS)
    correct = word
    list_word = list(word)
    # shuffle the word
    random.shuffle(list_word)
    print("What is the word?")
    for (i,val) in enumerate(list_word):
        print(val, end="")
    print()
    guess = input("Your answer:")
    points = 100
    while guess != correct and guess != "":
            print("Sorry, Try again.")
            help = input("Do you need help?")
            if help == "y" or help == "Y":
                points=int(points)-10
                if correct=="champion":
                    print("you won a final football match. You are..........")
                elif correct=="meticulous":
                    print("A word that shows great attention to detail")
                elif correct== "hexagon":
                    print("A figure with six straight sides and angles")
                elif correct=="difficult":
                    print("You don't know the answer. It is very..........")
            guess = input("Your guess: ")
    if guess == correct:
            print("Correct! You guessed it!\n")
            print("Your score is: "+str(points))
            play=input("Do you want to play again? (Y or N)")
    elif guess== "":
            print("You failed...")
            play=input("Do you want to play again? (yes or no)")

print("Thanks for playing.")