from passlib.hash import bcrypt
from time import sleep

# todo: create a dictionary to save and retrieve from the text file with student name as key and student id as value.
# todo: take student id values as keys in dictionary and store student line number as value
# todo: create dictionary studentid[course] to record grade per course

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

# dictionary of student names
with open("grades.txt", "a+", encoding ="utf-8") as f:
    f.seek(0)
    studentdict = f.readline(len(f.readline()) - 2)
    f.readline(2)
    coursedict = f.readline(len(f.readline()) - 2)
    f.readline(2)
    gradedict = f.readline(len(f.readline()) - 2)

# menu
# note: noi stands for name or id
while cont:
    menuselect = str(input("Choose number or letter:\n1. (A)dd grades\n2. (C)hange grades\n3. (R)emove grades\n4. (E)xit").replace(" ", "").lower())
    if menuselect == "a" or menuselect == "1":
        # ask for student name and id, ask for course, add grade for course, save to file, ask to cont
        name = input("Student name: ")
        id = int(input("Student ID: "))
        course = input("Student course: ")
        grade = input("Student grade: ")

        studentdict = studentdict | {name[id]}
        coursedict = coursedict | {id[course]}
        courseid = course + id
        gradedict = gradedict | {courseid[grade]}

    elif menuselect == "c" or menuselect == "2":
        # ask for student name or id, ask for course, find student (https://bit.ly/3Qfo0A9), edit grade for course,
        # save to file, ask to cont
        pass
    elif menuselect == "r" or menuselect == "3":
        # ask for student name or id, ask for course, remove grades, save to file, ask to cont
        pass
    elif menuselect == "e" or menuselect == "4":
        sure = input("Are you sure? (y/n): ").replace(" ", "").lower()
        if sure != "y":
            pass
        else:
            cont = False
print("Thank you. This program will close in 10 seconds.")
sleep(10)
quit()
