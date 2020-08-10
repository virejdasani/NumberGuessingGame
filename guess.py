
#  MADE BY:_            _   _____                        _
#  \ \    / (_)        (_) |  __ \                      (_)
#   \ \  / / _ _ __ ___ _  | |  | | __ _ ___  __ _ _ __  _
#    \ \/ / | | '__/ _ \ | | |  | |/ _` / __|/ _` | '_ \| |
#     \  /  | | | |  __/ | | |__| | (_| \__ \ (_| | | | | |
#      \/   |_|_|  \___| | |_____/ \__,_|___/\__,_|_| |_|_|
#                     _/ |
#                    |__/

# A Number Guessing Game

from random import randint

answer = randint(1, 9)

user_input = int(input("Guess any number between 0 and 10\n"))

while user_input != answer:
    if user_input > answer:
        user_input = int(input("The answer is smaller, Guess again\n"))


    elif user_input < answer:
        user_input = int(input("The answer is bigger, Guess again\n"))

    else:
        print("CORRECT!")

stringAnswer = str(answer)
print("CORRECT \nThe answer was: " + stringAnswer)
