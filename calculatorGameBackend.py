import random; import random as r

num1 = 0.0
num2 = 0.0
ans = 0.0
points = 0

def number1(lvl):
    global num1
    if lvl == "1" or lvl == "l":
        num1 = r.randint(1, 10)
    elif lvl == "2" or lvl == "m":
        num1 = r.randint(11, 50)
    elif lvl == "3" or lvl == "h":
        num1 = r.randint(51, 100)

def number2(lvl):
    global num2
    if lvl == "1" or lvl == "l":
        num2 = r.randint(1, 10)
    elif lvl == "2" or lvl == "m":
        num2 = r.randint(11, 50)
    elif lvl == "3" or lvl == "h":
        num2 = r.randint(51, 100)

def operate(oper, num1, num2):
    if oper == "a" or oper == "1":
        return float(num1 + num2)
    elif oper == "s" or oper == "2":
        return float(num1 - num2)
    elif oper == "m" or oper == "3":
        return float(num1 * num2)
    elif oper == "d" or oper == "4":
        return float(num1 / num2)

def game():
    oper = input(
        "What operation would you like to practice?\n1. (A)ddition\n2. (S)ubtraction\n3. (M)ultiplication\n4. (D)ivision\ntype letter or number: ").lower().strip()
    lvl = input(
        "At what level would you like to practice?\n1. (L)ow (1-10)\n2. (M)edium (11-50)\n3. (H)igh (51-100)\n type letter or number: ").lower().strip()
    numbr1 = number1(lvl)
    numbr2 = number2(lvl)
    rightans = operate(oper, numbr1, numbr2)

    operdict = {"a":"plus", "1":"plus", "s":"minus", "2":"minus", "m":"multiplied by", "3":"multiplied by", "d":"divided by", "4":"divided by"}

    ans = input(f"What is {numbr1} {operdict[lvl]} {numbr2}?: ")
    if ans == rightans:
        points += 1
        #ask to continue new quesiton
        cont = input("Correct. Continue to next question? (y/n): ").lower().strip()
        if cont == "y":
            game()
        else:
            print(f"You ended with {points} points.")
    else:
        retry = ("Incorrect. Try again?(y/n): ").lower().strip()
        if retry == "y":
            ans = input(f"What is {numbr1} {operdict[lvl]} {numbr2}?: ")
            if ans == rightans:
                points += 1
                # ask to continue new quesiton
                cont = input("Correct. Continue to next question? (y/n): ").lower().strip()
                if cont == "y":
                    game()
                else:
                    print(f"You ended with {points} points.")
            else:
                cont = (f"Incorrect. The correct answer was {rightans}. End game?(y/n): ").lower().strip()
                if cont == "y":
                    game()
                else:
                    print(f"You ended with {points} points.")

