import datetime as dt
import threading as th
import time as t
import keyboard as kb
import playsound as ps

# variables
timerAction = "Set"


# functions
def usrInput(displayedtext, itemtype):
	"""Supports strings and intergers. If string is selected, places input into str(input(usrinput)), while stripping
	 whitespaces and lowercasing letters. If integer is sel ected, returns int(input(usrinput))."""
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
		menu = f"{now.hour}:{now.minute}:{now.second} - Options: {timerAction} (T)imer - (B)ack - (Q)uit"
		back = "\b" + "\b" * len(menu)
		# printing options
		print(menu, end="")
		t.sleep(0.01)
		print(back, end="")
		if kb.is_pressed("t"):
			choice = "t"
			break
		elif kb.is_pressed("b"):
			break
		elif kb.is_pressed("q"):
			choice = "q"
			break
	# run stuff
	if choice == "t":
		if timerAction == "Set":
			timerStr = "Length of timer (in minutes, decimals allowed): "
			timerLen = usrInput(timerStr, "flo")
			timerBack = "\b" * len(timerStr) + "\b" * len(str(timerLen))
			secs = timerLen / 60.0
			timer = th.Timer(secs, ring)
			timer.start()
			print(timerBack)
			print(timerBack)
			timerAction = "Cancel"
		elif timerAction == "Cancel":
			timer.cancel()
			timerAction = "Set"
	elif choice == "q":
		run = False
		print("\b")

# todo: fix timer ringing immediately
# todo: fix timer not stopping after it's done
# todo: fix timer running immediately
