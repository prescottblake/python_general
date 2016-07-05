import random
countHeads = 0
countTails = 0
heads_tails =""
for count in range (1,5001):
	random_num = round(random.random())
	if random_num == 1:
		countHeads = countHeads +1
		heads_tails = "head"
	elif random_num == 0:
		countTails = countTails +1
		heads_tails = "tail"
	print "Attempt #" + str(count) + ": Throwing a coin... It's a " + heads_tails + "! ... Got " + str(countHeads) + "head(s) so far and " + str(countTails) + "tail(s) so far"
print "Ending the program, thank you!"