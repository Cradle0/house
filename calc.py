def mortgage_calc(principal,down,period,freq,rate):
	"""
	Args:
		principal (int): Total principal
		down (float): Down payment 0 <= down <=100
		period (int): Number of years of amort.
		freq (int): Payment frequency
		rate (float): Interest rate
	"""	
	down = down/100
	net_total = principal * (1-down)
	int_rate = interest_rate(rate,freq)
	if freq == "m":
		total_period = period * 12
		y = 1 - (1 + int_rate) ** (-total_period)
		payment = (net_total * int_rate) / y
		total_int = payment * total_period - net_total
	return payment, total_int
	

def interest_rate(rate,freq):
	"""
	Args:
		rate (float): annual 
		freq (str): m = monthly...
	"""	

	#semiannual
	rate = rate / 100
	rate  = rate / 2
	rate = 1 + rate
	rate = rate ** 2
	rate = rate ** (1/12) - 1
	return rate





