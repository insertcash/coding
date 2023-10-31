# to do list

# functions
def usrinput(usrinput, type):
    """Supports strings and intergers. If string is selected, places input into str(input(usrinput)), while stripping
     whitespaces and lowercasing letters. If integer is selected, returns int(input(usrinput))."""
    if type == "str":
        return str(input(usrinput)).strip().lower()
    elif type == "int":
        return int(input(usrinput))


# mainloop
run = True
while run:
    # read list from file
    with open("todo.txt", "r") as f:
        todo = f.readlines()

    # display list
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
        thing = usrinput("Item: ", "str")
        urgency = usrinput("Urgency (type 1-5): ", "str")
        saved = "`".join([thing, urgency])
        todo.append(saved + "\n")
        with open("todo.txt", "w") as f:
            f.truncate(0)
            f.writelines(todo)
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        print("Exiting...")
        run = False

