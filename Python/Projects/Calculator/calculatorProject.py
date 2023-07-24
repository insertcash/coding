# Create a simple calculator which can perform basic arithmetic operations like addition, subtraction,
# multiplication, or division depending upon the user input. Approach : User chooses the desired operation. Options
# 1, 2, 3, and 4 are valid. Two numbers are taken and an if…elif…else branching is used to execute a particular
# section. Using functions add(), subtract(), multiply() and divide() evaluate respective operations.


# accepting input


# defining addition, subtraction, etc
def add(a, b):
    return a + b


def sub(c, d):
    return c - d


def mul(e, f):
    return e * f


def div(g, h):
    return g / h


# computing
def calc():
    num1 = float(input("type first number here: "))
    operation = input(
        "will you (a)dd, (s)ubtract, (m)ultiply, or (d)ivide? (or: type 1, 2, 3, or 4 respectively): ").lower()
    num2 = float(input("type second number here: "))
    if operation == "a" or operation == "1":
        print("The answer is " + str(add(num1, num2)))
    elif operation == "s" or operation == "2":
        print("The answer is " + str(sub(num1, num2)))
    elif operation == "m" or operation == "3":
        print("The answer is " + str(mul(num1, num2)))
    elif operation == "d" or operation == "4":
        if num2 == 0.0:
            print("divide by zero error. run again")
        else:
            print("The answer is " + str(div(num1, num2)))
    else:
        print("something went wrong, likely because of user error. try running this again.")
    recalc = input("Calculate another problem? (y/n): ").lower()
    if recalc == "y":
        calc()


# running the calculator
calc()
