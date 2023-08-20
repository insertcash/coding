from passlib.hash import bcrypt
from time import sleep
import random as r

# Create a grading system for BSC computer science. The program should be able to capture the names, admission number
# and the student marks for the various course units they are taking. In addition to capturing the marks, the program
# should be able to grade all the units using the school of computing grading system. The students' details,
# the marks and the grade should be saved in a text file. The user of the system should also be able to view all the
# students' details saved in the file.
# The program should include a menu and an option to exit.

# A+ 97–100%
# A 93–96%
# A− 90–92%
# B+ 87–89%
# B 83–86%
# B− 80–82%
# C+ 77–79%
# C 73–76%
# C− 70–72%
# D+ 67–69%
# D 63–66%
# D− 60–62%
# F 0–59%

# verify
# accept username
user = "schooladmin"
userinput = input("Username: ").replace(" ", "")

# pass input
passwordinput = input("Password: ").replace(" ", "")

# hash
hasher = bcrypt.using()

# verify username and pass
correctuser = user == userinput
correctpass = hasher.verify(passwordinput, "$2b$12$nZ.MlsfIPNNyi/zvoLGBcuD017PhMTUNY7IRsu97uBzh6e2a3uEzO")

# quit if password is wrong
if not correctuser or not correctpass:
    # quit if password is wrong
    print("Sorry, incorrect username or password. This program will end in 10 seconds.")
    sleep(10)
    quit()
else:
    pass

# menu

cont = True
while cont:

    menuselect = str(input("Choose number or letter:\n1. (A)dd grades\n2. (C)hange grades\n3. (R)emove grades\n4. (V)iew grades\n5. (E)xit\n").replace(" ", "").lower())
    if menuselect == "a" or menuselect == "1":
        # ask for student name and admnum, ask for course, add grade for course, convert grade to letter, anchor grade, save to file

        # general input
        name = input("Student name: ")
        admnum = input("Student admission number: ")
        course = input("Student course: ")
        grade = input("Student grade: ")

        ac = admnum + "," + course

        # saving grade
        with open("grades.txt", "a+", encoding = "utf-8") as f:
            anchr = r.randint(1, 1000000)
            f.write(name + "," + ac + "," + grade + "," + str(anchr) + "\n")
            print(f"Student grade saved with label {anchr}. Using the label will be the only way to retrieve the grade.")

    elif menuselect == "c" or menuselect == "2":
        # ask for student grade anchr, edit grade/course/student name, etc., save to file
        anchr = input("Student grade label: ")

        # finding grade by anchr
        with open("grades.txt", "r") as f:
            for line in f:
                if str(anchr) in line:
                    print("Grade data found.")

        # refractor and print data
        data = line.split(",")
        # convert grade to letter
        if int(data[3]) >= 90:
            if int(data[3]) >= 97:
                ltrgrd = "A+"
            elif int(data[3]) >= 93:
                ltrgrd = "A"
            else:
                ltrgrd = "A-"
        elif int(data[3]) >= 80:
            if int(data[3]) >= 87:
                ltrgrd = "B+"
            elif int(data[3]) >= 83:
                ltrgrd = "B"
            else:
                ltrgrd = "B-"
        elif int(data[3]) >= 70:
            if int(data[3]) >= 77:
                ltrgrd = "C+"
            elif int(data[3]) >= 73:
                ltrgrd = "C"
            else:
                ltrgrd = "C-"
        elif int(data[3]) >= 60:
            if int(data[3]) >= 67:
                ltrgrd = "D+"
            elif int(data[3]) >= 63:
                ltrgrd = "D"
            else:
                ltrgrd = "D-"
        else:
            ltrgrd = "F"
        print(
            f"Student name: {data[0]}\nStudent admission number: {data[1]}\nStudent course: {data[2]}\nStudent grade: {data[3]}\nStudent letter grade: {ltrgrd}\nStudent grade label: {data[4]}\n")
        chngdatatrue = input("Do you want to change the grade? (y/n): ").replace(" ", "").lower()
        if chngdatatrue == "y":
            chngdata = input("New grade: ").replace(" ", "")
            data[3] = chngdata
        else:
            pass

    elif menuselect == "r" or menuselect == "3":
        # ask for anchr, remove grades, save to file
        anchr = input("Student grade label: ")

        # finding grade by anchr
        with open("grades.txt", "r") as f:
            for line in f:
                if str(anchr) in line:
                    print("Grade data found.")
                    currentline = f.tell()
                    linelen = len(line)
        with open("grades.txt", "w") as f:
            f.seek(currentline)
            overwrite = "-" * (linelen - 2)
            f.write(overwrite)

    elif menuselect == "v" or menuselect == "4":
        # ask for anchr, find place, return data
        anchr = input("Student grade label: ")

        # finding grade by anchr
        with open("grades.txt", "r") as f:
            for line in f:
                if str(anchr) in line:
                    print("Grade data found.")

                # refractor and print data
                data = line.split(",")
                # convert grade to letter
                if int(data[3]) >= 90:
                    if int(data[3]) >= 97:
                        ltrgrd = "A+"
                    elif int(data[3]) >= 93:
                        ltrgrd = "A"
                    else:
                        ltrgrd = "A-"
                elif int(data[3]) >= 80:
                    if int(data[3]) >= 87:
                        ltrgrd = "B+"
                    elif int(data[3]) >= 83:
                        ltrgrd = "B"
                    else:
                        ltrgrd = "B-"
                elif int(data[3]) >= 70:
                    if int(data[3]) >= 77:
                        ltrgrd = "C+"
                    elif int(data[3]) >= 73:
                        ltrgrd = "C"
                    else:
                        ltrgrd = "C-"
                elif int(data[3]) >= 60:
                    if int(data[3]) >= 67:
                        ltrgrd = "D+"
                    elif int(data[3]) >= 63:
                        ltrgrd = "D"
                    else:
                        ltrgrd = "D-"
                else:
                    ltrgrd = "F"
                print(
                    f"Student name: {data[0]}\nStudent admission number: {data[1]}\nStudent course: {data[2]}\nStudent grade: {data[3]}\nStudent letter grade: {ltrgrd}\nStudent grade label: {data[4]}\n")

    elif menuselect == "e" or menuselect == "5":
        # exit program
        # ask for confirmation
        sure = input("Are you sure? (y/n): ").replace(" ", "").lower()
        if sure != "y":
            pass
        else:
            cont = False
print("Thank you. This program will close in 10 seconds.")
sleep(10)
quit()
