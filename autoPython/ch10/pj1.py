#!/usr/bin/python3

import random
guess = ''
answer = ('heads', 'tails')
while guess not in answer:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = answer[random.randint(0,1)] # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
