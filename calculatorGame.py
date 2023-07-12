# Create a game that will help primary school children practice with arithmetic. The program should have a menu that
# the learner will choose what operation they want to practice with (Addition, subtraction, division and
# multiplication). The learner should be able to choose the level he wants to play with. (Low level has numbers
# between 1-10, mid-level has numbers between 11-50 and high level has numbers between 51-100). Once the learner
# chooses the levels, and the operation to practice with, the program should generate two random numbers for the
# learner to give an answer to the operation selected. If the answer is correct the learner earns a 1 point. If the
# answer is wrong the program should display the correct answer to the learner. The program should enable the learner
# play as many times as they wish. When the learner has finished playing, the program should be able to display the
# total points earned.

import random; import random as r

# variables
operInp = input("What operation woud you like to learn:\n1. (A)ddition\n2. (S)ubtraction\n3. (M)ultiplication\n4.(D)ivision\n(type either the letter, or 1-4): ").lower()
level = input("What level would you like to work at?\n1. (L)ow: (1-10)\n2. (M)edium: (11-50)\n3. (H)igh: (51-100)\ninput here: ").lower()

low = tuple(range(1, 11))
med = tuple(range(11, 51))
hi = tuple(range(51, 101))

def game(oper, lvl):
    a = 0
    b = 0
    if level == "l" or level == "1":
    a = r.choice(low)
    b = r.choice(low)
