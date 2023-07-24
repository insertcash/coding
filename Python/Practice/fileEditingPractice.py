# if you open a file using f.open() without using a with statement, remember to f.close() it or else your computer die
# f.seek() will move the cursor by character
with open("test.txt", "a+", encoding ="utf-8") as f:
    # lines = ["this\n", "is\n", "being\n", "written\n", "from\n", "python!!!\n", ":)\n", ]
    # f.writelines(lines)

    # print(f.tell())

    f.seek(6)

    # f.readline() will read everything else on that line
    print(f.readline(), end = "")