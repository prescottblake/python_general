
for count in range(1,2001):
	odd_even = ""
	if count%2 == 1:
		odd_even = "odd"
	if count%2 == 0:
		odd_even = "even"
	print "Number is " + str(count) + ".  This is an "+ odd_even +" number."