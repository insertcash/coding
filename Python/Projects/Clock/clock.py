import datetime as dt
import playsound as ps
import keyboard as kb
import time as t
import threading as th

# variables
timerAction = "Set"
alarmAction = "Set"
alarmRunning = False


# functions
def usrInput(displayedtext, itemtype):
    """Supports strings and intergers. If string is selected, places input into str(input(usrinput)), while stripping
     whitespaces and lowercasing letters. If integer is selected, returns int(input(usrinput))."""
    if itemtype == "str":
        return str(input(displayedtext)).strip().lower()
    elif itemtype == "int":
        return int(input(displayedtext))
    elif itemtype == "flo":
        return float(input(displayedtext))


def ring():
    ps.playsound("arches.wav")


# mainloop
run = True
while run:
    # time loop
    while True:
        # getting time
        now = dt.datetime.now()
        time = f"The time is {now.hour}:{now.minute}:{now.second}, on {now.month}/{now.day}/{now.year}. Press o for options."
        back = "\b" + "\b" * len(time)
        # printing time + option for menu
        print(time, end="")
        t.sleep(0.01)
        print(back, end="")
        if kb.is_pressed("o"):
            break

    # option loop
    while True:
        # getting time
        now = dt.datetime.now()
        menu = f"{now.hour}:{now.minute}:{now.second} - Options: {timerAction} (T)imer - {alarmAction} (A)larm - (B)ack - (Q)uit"
        back = "\b" + "\b" * len(menu)
        # printing options
        print(menu, end="")
        t.sleep(0.01)
        print(back, end="")
        if kb.is_pressed("t"):
            choice = "t"
            break
        elif kb.is_pressed("a"):
            choice = "a"
            break
        elif kb.is_pressed("b"):
            break
        elif kb.is_pressed("q"):
            choice = "q"
            break
        if alarmRunning:
            if alarmDigits[0] == now.hour:
                if int(alarmDigits[1]) == now.minute:
                    ring()

    # run stuff
    if choice == "t":
        if timerAction == "Set":
            timerStr = "Length of timer (in minutes, decimals allowed): "
            timerLen = usrInput(timerStr, "flo")
            timerBack = "\b" * len(timerStr) + "\b" * len(str(timerLen))
            secs = timerLen/60
            timer = th.Timer(secs, ring)
            timer.start()
            timerAction = "Cancel"
        elif timerAction == "Cancel":
            timer.cancel()
            timerAction = "Set"
    elif choice == "a":
        if alarmAction == "Set":
            alarmStr = "When to ring alarm (hr:mm format): "
            alarmTime = usrInput(alarmStr, "str")
            back = "\b" * len(alarmStr) + "\b" * len(alarmTime)
            alarmDigits = alarmTime.split(":")
            alarmRunning = True
            print(back)
            alarmAction = "Cancel"
        elif alarmAction == "Cancel":
            alarmRunning = False
            alarmAction = "Set"
    elif choice == "q":
        run = False
        print("\b")

# todo: fix timer ringing immediately
# todo: fix alarm not ringing
