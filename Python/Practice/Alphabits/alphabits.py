# From this string- 'abcdefghijklmnopqrstuvwxyz'
# Produce "Aa Bb Cc..."
# Note to self, this entire practice project started because I was too lazy to type out "Aa Bb..." so I could test fonts on Google fonts.
# Good learing though, challenging practice

alphabet = "abcdefghijklmnopqrstuvwxyz"

lower = list(alphabet)

upper = []

for i in range(len(lower)):
	upper.append(lower[i].upper())

tick = 0
count = 0
alphabetList = []

for i in range(len(alphabet * 3)):
	if tick == 0:
		alphabetList.append(upper[count])
		tick += 1
	elif tick == 1:
		alphabetList.append(lower[count])
		tick += 1
	elif tick == 2:
		alphabetList.append(" ")
		tick = 0
		count += 1
	else:
		print("Error: Tick isn't 0, 1, or 2.")

alphabits = "".join(alphabetList)
print(alphabits)
