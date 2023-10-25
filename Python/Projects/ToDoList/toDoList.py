# to do list

# imports
import random as r

# functions
def usrinput(usrinput, type):
    """Supports strings and intergers. If string is selected, places input into str(input(usrinput)), while removing
     whitespaces and lowercasing letters. If interger is selected, returns int(input(usrinput)), while removing
     whitespaces."""
    if type == "str":
        return str(input(usrinput)).replace(" ", "").lower()
    elif type == "int":
        return int(input(usrinput)).replace(" ", "")

# show list
# read list from file
with open("todo.txt", "r") as f:
    todo = f.readlines()

# mainloop
run = True
while run:
    # display list
    if not todo:
        count = 0
        items = []
        for i in todo:
            count += 1
            item = i.split("`")
            items.append(f"{count}. {item[0]} - urgency {item[1]}")
            print(f"{count}. {item[0]} - urgency {item[1]}")
    else:
        print("Congrats! You have no items in your todo list!")

    # show options
    menu = usrinput("Options:\n1. Add item(s)\n2. Complete item(s)\n3. Change an item\n4. Exit\nSelect by number: ", "str")
    if menu == "1":
        bulk = usrinput("Add in bulk?(y/n): ", "str")
        if bulk == "y":
            pass
            # TODO: ensure to finish the bulk functionality for adding items
        elif bulk == "n":
            item = usrinput("Item: ", "str")
            urgency = usrinput("Urgency(number 1-5, 1 is most urgent): ", "int")
            with open("todo.txt", "a") as f:
                f.write(f"{item}`{urgency}\n")
            print("Item added successfully!")
        else:
            print("Invalid command.")
            continue
    if menu == "2":
        bulk = usrinput("Add in bulk?(y/n): ", "str")
        if bulk == "y":
            pass
            # TODO: ensure to finish the bulk functionality for removing items
        elif bulk == "n":
            line = usrinput("Item number: ", "int") - 1
            with open("todo.txt", "r") as f:
                lines = f.readlines()
            lines.remove(items[line])
            with open("todo.txt", "w") as f:
                f.truncate()
                f.writelines(line)
