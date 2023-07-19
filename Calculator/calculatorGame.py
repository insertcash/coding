import random
import random as r

num1 = 0.0
num2 = 0.0
ans = 0.0
points = 0


def number(lvl):
    global num1
    if lvl == "1" or lvl == "l":
        return r.randint(1, 10)
    elif lvl == "2" or lvl == "m":
        return r.randint(11, 50)
    elif lvl == "3" or lvl == "h":
        return r.randint(51, 100)


def operate(oper, num1, num2):
    if oper == "a" or oper == "1":
        return float(num1) + float(num2)
    elif oper == "s" or oper == "2":
        return float(num1) - float(num2)
    elif oper == "m" or oper == "3":
        return float(num1) * float(num2)
    elif oper == "d" or oper == "4":
        return float(num1) / float(num2)


contGame = True
while contGame:
    oper = input(
        "What operation would you like to practice?\n1. (A)ddition\n2. (S)ubtraction\n3. (M)ultiplication\n4. (D)ivision\ntype letter or number: ").lower().strip()
    lvl = input(
        "At what level would you like to practice?\n1. (L)ow (1-10)\n2. (M)edium (11-50)\n3. (H)igh (51-100)\ntype letter or number: ").lower().strip()
    numbr1 = number(lvl)
    numbr2 = number(lvl)
    rightans = operate(oper, numbr1, numbr2)

    operdict = {"a": "plus", "1": "plus", "s": "minus", "2": "minus", "m": "multiplied by", "3": "multiplied by",
                "d": "divided by", "4": "divided by"}

    ans = float(input(f"What is {numbr1} {operdict[lvl]} {numbr2}?: "))
    if ans == rightans:
        points += 1
        # ask to continue new quesiton
        cont = input("Correct. Continue to next question? (y/n): ").lower().strip()
        if cont == "y":
            continue
        else:
            print(f"You ended with {points} points.")
            break
    else:
        retry = input("Incorrect. Try again? (y/n): ").lower().strip()
        if retry == "y":
            while retry == "y":
                ans = float(input(f"What is {numbr1} {operdict[lvl]} {numbr2}?: "))
                if ans == rightans:
                    points += 1
                    # ask to continue new quesiton
                    cont = input("Correct. Continue to next question? (y/n): ").lower().strip()
                    if cont == "y":
                        continue
                    else:
                        print(f"You ended with {points} points.")
                        break
    break
print("Thank you for playing.\nGoodbye!")
