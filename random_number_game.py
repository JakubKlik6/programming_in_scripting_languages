print("Social security number check\n")
print("If you want to exit the game choose 0\n")

userInput = input("enter your social security number... ")

if len(userInput) == 9:
    while True:
        try:
            userInputAsNumber = int(userInput)

        except:
            print("Wrong value!")
            userInput = input("Guess the number... ")
else:
    print("Wrong input!")

