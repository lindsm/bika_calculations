def total_d3(d2_raw, d3_raw, d2_factor, d3_factor):
	""" (number, number, number, number)  --> integer

	Return the integer value of d3_raw divided by d3_factor plus d2_raw divided by d2_factor if d2_raw is greater than 1.95.  If d2_raw is less than 1.96 then return d3_raw divided by d3_factor.


	>>>total_d3(5.3677, 31.74, 1.18, 1.28)
	29	
	"""

	if d2_raw > 1.95:  #If the D2 value is less than 1.96 ignore it and return the D3 value by itself as an integer.
		return int(round(d2_raw / d2_factor, 2) + round(d3_raw / d3_factor, 2))
	else:
		return int(round(d3_raw / d3_factor, 0))

print total_d3(5.3677, 31.74, 1.18, 1.28)