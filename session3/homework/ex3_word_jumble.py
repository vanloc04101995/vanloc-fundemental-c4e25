import random
# create a sequence of words to choose from
WORDS = ("champion", "meticulous", "hexagon", "difficult")
print(" Welcome to Word Jumble!")
play=input("Do you want to play? (Y or N)")
while play=="y" or play=="Y":
    # pick a random word in the list
    word = random.choice(WORDS)
    correct = word
    jumble =""
    while word: # trong khi word vẫn còn kí tự thì n vẫn là true, đến khi n Null là False
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    print("What is the word?", jumble)
    points=100
    guess = input("\nYour answer: ")
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
