import random
randNum = random.randint(1,100)
userGuess = None
gusses = 0

while (userGuess != randNum):
    userGuess = int(input("Enter an number: "))
    if (userGuess == randNum):
        print("congrats! You guess it right")
    else:
        if (userGuess>randNum):
            print("Enter an smaller number")
        else:
            print("Enter an larger number")
    gusses += 1  
print(f"Your guess it right in {gusses} gusses")

with open("New_Hiscore.txt","r") as f:
    Hiscore = int(f.read())

if Hiscore == "":
    with open("New_Hiscore.txt",'w') as f:
        f.write(str(gusses))

if gusses<Hiscore:
    print("You just have Broken the hiscore")
    with open("New_Hiscore.txt","w") as f:
        f.write(str(gusses))
