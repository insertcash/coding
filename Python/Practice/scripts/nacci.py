import time as t
import sys

# FOR THE LOVE OF PERFECTLY RUNNING THE CODE FIRST TRY
# RUN THIS CODE IN DEBUG IF YOU TRY TO REACH THE MAXIMUM INTEGER
# YOU MUST BE ABLE TO PAUSE OR BE ABLE TO TOLERATE YOUR COMPTER TURNING INTO A JET ENGINE

sys.set_int_max_str_digits(2147483647)


def fibbonaci():
	a = 0
	b = 1
	count = 0
	while True:
		t.sleep(0)
		count += 1
		a, b = b, a + b
		return f"{count}: {b}"


fibbonaci()
