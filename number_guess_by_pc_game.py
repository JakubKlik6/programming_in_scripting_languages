import random

print("Hello in number check game, when you enter your number, and computer will try to guess it! :)\n")


def input_to_number(number):
    try:
        num = int(number)
        return num
    except ValueError:
        print(print(f"{number} is incorrect social security number"))


def user_answer_check(answer):
    if answer == "more":
        return 1
    elif answer == "less":
        return 0
    else:
        print("Wrong input :(")


def subtraction(number):
    if number > 10:
        return number - 5
    else:
        return number


user_input = input("Enter your number! ... ")

user_input_as_number = input_to_number(user_input)

print("\nSo now computer will try to guess your number")
print("All you need to do is to tell him less or more\n")
print("Also, if you want to quit, just enter exit :)\n")

computer_guess = random.randint(0, user_input_as_number + 250)
dif_num = 100

while computer_guess != user_input_as_number:
    print(f"PC -> is it ... {computer_guess} ??\n")
    user_answer = input("...")
    if user_answer == "quit":
        break
    else:
        num = user_answer_check(user_answer)
        if num == 1:
            computer_guess = random.randint(computer_guess, computer_guess + dif_num)
            dif_num = subtraction(dif_num)
        elif num == 0:
            computer_guess = random.randint(computer_guess - dif_num, computer_guess)
            dif_num = subtraction(dif_num)

print(f'Computer WON :), your number is {computer_guess}')
