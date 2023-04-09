import random

print("Hello player! Welcome to Try to guess the number game!\n")
print("If you want to exit the game choose 0\n")

userInput = input("Guess the number... ")
number = random.randint(1, 1000)

while True:
    try:
        userInputAsNumber = int(userInput)
        if userInputAsNumber == 0:
            print("\nGame over\n")
            break
        if userInputAsNumber == number:
            print("You won")
            break
        elif userInputAsNumber < number:
            print("A little bit more")
            userInput = input("Guess the number... ")
        elif userInputAsNumber > number:
            print("A little bit less")
            userInput = input("Guess the number... ")
    except:
        print("Wrong value!")
        userInput = input("Guess the number... ")
