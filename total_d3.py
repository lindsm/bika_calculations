def total_d3(d2,d3,d2f,d3f):
	"""Return the total value of D3 based on given criteria"""
	#example
	#total_d3(5.3677,31.74,1.18,1.28) --> 29

	if d2 < 1.96:  #If the D2 value is less than 1.96 ignore it and return the D3 value by itself as an integer.
		return int(round(d3,0))
	else:
		return int(round(d2/d2f,2) + round(d3/d3f,2))

print total_d3(5.3677,31.74,1.18,1.28)