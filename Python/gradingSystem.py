from passlib.hash import bcrypt
from time import sleep

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
userinput = input("Username: ")

# pass input
pswdinput = input("Password: ")

# hash
hshr = bcrypt.using()

# verify username and pass
correctuser = user == userinput
correctpass = hshr.verify(pswdinput, "$2b$12$nZ.MlsfIPNNyi/zvoLGBcuD017PhMTUNY7IRsu97uBzh6e2a3uEzO")

# quit if password is wrong
if not correctuser and correctpass:
    print("Sorry, incorrect username or password. This program will end in 10 seconds.")
    sleep(10)
    quit()
else:
    pass

# menu