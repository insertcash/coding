# to do list

# functions
def usrinput(displayedtext, itemtype):
    """Supports strings and intergers. If string is selected, places input into str(input(usrinput)), while stripping
     whitespaces and lowercasing letters. If integer is selected, returns int(input(usrinput))."""
    if itemtype == "str":
        return str(input(displayedtext)).strip().lower()
    elif itemtype == "int":
        return int(input(displayedtext))


# mainloop
run = True
while run:
    # read list from file
    with open("todo.txt", "r") as f:
        todo = f.readlines()

    # display list
    print("List of items:")
    count = 0
    for i in todo:
        # reads and splits the item on the to do list. then, prints the item, and ups the count.
        item = todo[count]
        item = item.split("`")
        if count == len(todo) - 1:
            print(f"{count + 1}. {item[0]} - urgency {item[1]}")
        else:
            print(f"{count + 1}. {item[0]} - urgency {item[1]}", end="")
        count += 1
        if count == len(todo):
            break

    menu = usrinput("Options:\n1. Add item\n2. Complete item\n3. Edit item\n4. Exit\nSelect by number: ", "int")
    if menu == 1:
        # get info about item
        thing = usrinput("Item: ", "str")
        urgency = usrinput("Urgency (type 1-5): ", "str")
        saved = "`".join([thing, urgency])
        # save item to file
        todo.append(saved + "\n")
        with open("todo.txt", "w") as f:
            f.truncate(0)
            f.writelines(todo)
        print("Item was saved successfully.")

    elif menu == 2:
        # get item to remove
        num = usrinput("Complete item by number in list: ", "int") - 1
        del todo[num]
        # save file
        with open("todo.txt", "w") as f:
            f.truncate(0)
            f.writelines(todo)
        print("Item was completed successfully.")

    elif menu == 3:
        # get info about item
        num = usrinput("Item to change in list: ", "int") - 1
        thing = usrinput("Item: ", "str")
        urgency = usrinput("Urgency (type 1-5): ", "str")
        changed = "`".join([thing, urgency])
        # save item to file
        todo[num] = changed + "\n"
        with open("todo.txt", "w") as f:
            f.truncate(0)
            f.writelines(todo)
    elif menu == 4:
        print("Exiting...")
        run = False
