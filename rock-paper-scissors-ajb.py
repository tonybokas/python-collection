'''This is the game Rock, Paper, Scissors.'''

import random, sys

print('ROCK, PAPER, SCISSORS!')

# The following variables keep score:
wins = 0
losses = 0
ties = 0

while True: # starts the main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # starts the player input loop.
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quits the game.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # ends the player input loop.
        print('Type either (r), (p), or (s) to choose an implement. Otherwise, type (q) to exit.')
    
    # The following displays the player's selection:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # The following displays the computer's selection:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove == 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove == 's'
        print('SCISSORS')
        
    # The following displays and records the score.
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You won!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You won!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You won!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lost!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lost!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lost!')
        losses = losses + 1