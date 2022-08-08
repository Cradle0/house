import calc
import os

def main():
	valid = False
	while not valid:
		try:
			principal = float(input("Principal amount: "))
			down = float(input("Down: "))
			period = int(input("Number of years: "))
			rate = float(input("Interest rate: "))
			valid = True
		except ValueError:
			print("Numbers only")
	valid = False
	while not valid:
		freq = str(input("Input m for monthly: "))
		if freq != "m":
			print("m please")
		else:
			valid = True
	print(calc.mortgage_calc(principal,down,period,freq,rate))

if __name__ == "__main__":
    main()

