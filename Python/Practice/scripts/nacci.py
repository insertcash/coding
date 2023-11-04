import time as t


def fibbonaci():
    a = 0
    b = 1
    count = 0
    while True:
        count += 1
        a, b = b, a + b
        print(f"{count}: {b}")
        t.sleep(0.25)


fibbonaci()
