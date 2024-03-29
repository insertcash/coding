from termcolor import colored as clr
print(clr("TTTTTT III  CCC     TTTTTT  AA   CCC     TTTTTT  OOO  EEEE \n  TT    I  C          TT   A  A C          TT   O   O E    \n  TT    I  C          TT   AAAA C          TT   O   O EEE  \n  TT    I  C          TT   A  A C          TT   O   O E    \n  TT   III  CCC       TT   A  A  CCC       TT    OOO  EEEE ", "red"))

play = input("Play? (Y/N): ").upper().strip()
if play == "Y":
	pass
else:
	quit()

