
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

while True:
    if user_input == answer:
        print("CORRECT")
        user_input = int(input(""))

    elif user_input > answer:
        print("The number is smaller, Guess Again")
        user_input = int(input(""))

    elif user_input < answer:
        print("The number is bigger, Guess Again")
        user_input = int(input("")) 
       
          
