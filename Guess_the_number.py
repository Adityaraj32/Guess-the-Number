# guees_number = 18
# guees = 0

# while True:
#     guees += 1    
#     userinput = int(input("Enter an number: "))
#     # userinput = raw_input("Enter an number: ") # not confirm what is this 
#     if userinput > guees_number:
#         print(f"You have {9 - guees} guees left")
#         print("Enter the smaller number")
#     elif userinput < guees_number:
#         print(f"You have {9 - guees} guees left")
#         print("Enter the greter number")
#     elif userinput == guees_number:
#         print("Congrats! You won")
#         break
#     if guees == 9:
#         print(f"You have completed this game in {guees} guees")
#         print("The guess are are completed")
#         break
# print(guees)


# making using for loop

import random
guess_number2 = random.randint(1, 100) #you can user for only intertainment purpose
# guess_number2 = 18
guess2 = 0
max_guess = 9
game_over = False
print("This is guess the number game")
print("Enter number from 1 to 100\n")

# for attemt in range(game_over):
# while game_over == False:
while not game_over:
    user_input2 = int(input("Enter an number: "))
    if user_input2 > 100:
        print("Plese write number less than 100 or 100\n")
        continue
    guess2 += 1
    if guess2 == 9:
        print("Game over! your life is over")
        # break
        game_over = True
    elif user_input2 > guess_number2:
        print(f"Enter Smaller number                                               life:{9 - guess2} \n")
    elif user_input2 < guess_number2:
        print(f"Enter Larger number                                               life:{9 - guess2} \n")
    elif user_input2 == guess_number2:
        print("Congrats! you win")
        print(f"You have completed this game in {guess2}")
        # break
        game_over = True