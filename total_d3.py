def total_d3(d2,d3,d2f,d3f):
	"""Return the total value of D3 based on given criteria"""

	#total_d3(5.3677,31.74,1.18,1.28) --> 29
	d2 = round(d2,2)
	d3 = round(d3,2)

	print round(d2/d2f,2)
	print round(d3/d3f,2)

	if d2 < 1.96:
		return int(round(d3,0))
	else:
		return int(round(d2/d2f,2) + round(d3/d3f,2))

print total_d3(5.3677,31.74,1.18,1.28)