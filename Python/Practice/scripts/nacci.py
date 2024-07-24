import time as t
import sys

sys.set_int_max_str_digits(2147483647)


def fibbonaci():
	a = 0
	b = 1
	count = 0
	while True:
		t.sleep(0)
		count += 1
		a, b = b, a + b
		print(f"{count}: {b}")


fibbonaci()
