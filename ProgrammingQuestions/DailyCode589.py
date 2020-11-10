#Good morning! Here's your coding interview problem for today.
#This problem was asked by Two Sigma.
#Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.
#The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.
#The second game: same, except that the stopping condition is a five followed by a five.
#Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

import random

N = 10000

score =  0
for i in range(N):
    last_number = 0 
    while True:
        score += 1
        number = random.randint(1,6)
        if last_number == 5 and number ==6:
            break
        last_number = number
print(score/N)

score =  0
for i in range(N):
    last_number = 0 
    while True:
        score += 1
        number = random.randint(1,6)
        if last_number == 5 and number == 5:
            break
        last_number = number
print(score/N)

#Better to play game 1
