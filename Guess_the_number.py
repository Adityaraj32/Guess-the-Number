import random
guess_number2 = random.randint(1, 100)
guess2 = 0
max_guess = 9
game_over = False
print("This is guess the number game")
print("Enter number from 1 to 100\n")

while not game_over:
    user_input2 = int(input("Enter an number: "))
    if user_input2 > 100:
        print("Plese write number less than 100 or 100\n")
        continue
    guess2 += 1
    if guess2 == 9:
        print("Game over! your life is over")
        game_over = True
    elif user_input2 > guess_number2:
        print(f"Enter Smaller number                                               life:{9 - guess2} \n")
    elif user_input2 < guess_number2:
        print(f"Enter Larger number                                               life:{9 - guess2} \n")
    elif user_input2 == guess_number2:
        print("Congrats! you win")
        print(f"You have completed this game in {guess2}")
        game_over = True
