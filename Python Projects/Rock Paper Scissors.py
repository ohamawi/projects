import random

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")


    choice = int(input("Enter your choice1 :"))

    while choice > 3 or choice < 1:
        choice = int(input('Please input something that works.'))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('You chose \n', choice_name)
    comp_choice = random.randint(1, 3)
    
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    print("The other guy chose \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if choice == comp_choice:
        print('GODDAMN IT IT WAS A DRAW', end="")
        result = "DRAW"
    if (choice == 1 and comp_choice == 2):
        print("I guess the Rock wasn't that strong after all =>", end="")
        result = 'papeR'
    elif (choice == 2 and comp_choice == 1):
        print('You beat the Rock? That goes against the contract... =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock beats metal, somehow... =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('You bashed a pair of scissors to death. Nice dingus. =>\n', end="")
        result = 'rocK'

    if (choice == 2 and comp_choice == 3):
        print('Bro you got origami-ed =>', end="")
        result = 'scissoR'
    elif (choice == 3 and comp_choice == 2):
        print('Can not believe you stabbed that paper in the esophagus. =>', end="")
        result = 'Rock'
    if result == 'DRAW':
        print("<== You fucking tied the bot? Really? ==>")
    if result == choice_name:
        print("<== You win. Wow. ==>")
    else:
        print("<== You lost to literal RNG. Classy. ==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing! Have a good one, shitter!")