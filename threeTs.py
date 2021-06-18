import tkinter as tk

def placeLet(letter, pos):
    board[pos] = letter

def freeSpace(pos):
    return board[pos] == ' '

def printBoard(board):
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')

def winner(b,ltr):
    return (b[7] == ltr and b[8] == ltr and b[9] == ltr) or (b[4] == ltr and b[5] == ltr and b[6] == ltr) or (b[1] == ltr and b[2] == ltr and b[3] == ltr) or (b[1] == ltr and b[5] == ltr and b[9] == ltr) or (b[3] == ltr and b[5] == ltr and b[7] == ltr) or (b[1] == ltr and b[4] == ltr and b[7] == ltr) or (b[2] == ltr and b[5] == ltr and b[8] == ltr) or (b[3] == ltr and b[6] == ltr and b[9] == ltr)

def player():
    run = True
    while run:
        move = input('Which space would you like to choose? (1-9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freeSpace(move):
                    run = False
                    placeLet('X', move)
                else:
                    print('This place is already filled, please select another from 1-9')
            else:
                print('Please enter a number within the range 1-9')
        except:
            print('Please enter a number between 1 and 9')

def CPU():
    possMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    cornOpen = []
    for i in possMoves:
        if i in [1,3,7,9]:
            cornOpen.append(i)
    if len(cornOpen) > 0:
        move = chooseRand(cornOpen)
        return move

    if 5 in possMoves:
        move = 5
        return move
    
    edgeOpen = []
    for i in possMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    if len(edgeOpen) > 0:
        move = chooseRand(edgeOpen)
    
    return move

def chooseRand(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def fullBoard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Tic-Tac-Toe')
    printBoard(board)

    while not(fullBoard(board)):
        if not(winner(board,'O')):
            player()
            printBoard(board)
        else:
            print('CPU won the game')
            timesOwon.append(1)
            break

        if not(winner(board,'X')):
            move = CPU()
            if move == 0:
                print('It\'s a draw!')
            else:
                placeLet('O',move)
                print('CPU took it\'s turn on space', move,':')
                printBoard(board)
        else:
            print(name,'won the game, Congrats!')
            timesXwon.append(1)   
            break

    if fullBoard(board):
        print('The game is tied!')


print('Welcome to Tic-Tac-Toe!')
name = input('What is your name?')
board = [' ' for x in range(10)] 
timesXwon = []
timesOwon = [] 
main()

while True:
    play = str(input('Want to play Tic-Tac-Toe? (Y/N)'))
    if play == 'Y' or play =='y':
        board = [' ' for x in range(10)] 
        main()
    else:
        print('Final Score:', name,':', len(timesXwon), '   CPU :', len(timesOwon))
        print('Thanks for playing!')
        exit()