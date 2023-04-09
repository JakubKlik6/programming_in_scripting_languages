def sum_check(number):
    check_numbers = [1, 3, 7, 9] * 3
    digits = [int(i) for i in str(number)]
    sum_list = sum(i * f for i, f in zip(digits, check_numbers))
    return sum_list % 10


def is_valid_number(number):
    if not isinstance(number, int):
        return False  # is number integer?
    if len(str(number)) != 11:
        return False  # is number has 11 digits
    if not str(number).isdigit():
        return False  # is number made of digits only?
    return True  # if number is correct


def input_to_number(number):
    try:
        num = int(number)
        return num
    except ValueError:
        print(f"{number} is incorrect social security number")
        return None


while True:
    user_input = input("Enter your social security number... ")
    if user_input == "q":
        break

    user_input_as_number = input_to_number(user_input)

    if is_valid_number(user_input_as_number):
        last_digit = sum_check(user_input_as_number)
        if last_digit != 0:
            print("The social security number is invalid")
        else:
            print("The social security number is valid")
            break
