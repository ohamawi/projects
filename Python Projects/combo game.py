import random
def hangmangame():
    name = input("What is your name? ")

    print("Hello, " + name, "Time to play hangman!")

    print("Start guessing...")

    word = ("Skyrim").lower()

    guesses = ('')

    turns = 10

    while turns > 0:
        failed = 0
        for char in word:

            if char in guesses:
                print(char, end=""),

            else:
                print("_", end=""),
                failed += 1
        if failed == 0:
            print(" You won")
            break
        guess = input("guess a letter:").lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            if turns == 0:
                print("You Lose")

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def tictactoegame():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        if turn == 'X':
            print("It's your turn," + turn + ". Move to which place?")
            move = input()
        else:
            print("AI's turn. Move to which place?")
            move = random.choice([key for key in board_keys if theBoard[key] == ' '])
            print(move)

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            if turn == 'X':
                print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(turn + " won.")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        tictactoegame()


best_of_5 = 0

while best_of_5 < 5:
    which_game = input("Which game would you like to play? (H)angman or (T)ic Tac Toe? ")
    if which_game == 'h':
        hangmangame()
        best_of_5 += 1
    elif which_game == 't':
        tictactoegame()
        best_of_5 += 1
    else:
        print("Please input a valid program")