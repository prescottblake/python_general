print "Scores and Grades"
for count in range(1,11):
	grade =""
	print "Score: "
	score = input()
	if score >= 60 and score <= 69:
		grade = "D"
	elif score >= 70 and score <=79:
		grade = "C"
	elif score >= 80 and score <= 89:
		grade = "B"
	elif score >= 90:
		grade = "A"
	else: 
		grade = "You Failed"
	print "Your grade is " + grade