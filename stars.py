# def draw_stars(x):
# 	for element in x:
# 		starCount = ""
# 		for count in range (0, element):
# 			starCount += "*"
# 		print starCount

# x = [4,6,1,3,5,7,25]
# draw_stars(x)

def draw_stars(x):
	for element in x:
		if type(element) is str:
			printedChar = element[0]
			stringPrint = ""
			for count in range(0, len(element)):
				stringPrint += printedChar
			print stringPrint
		if type(element) is int:
			starCount = ""
			for count in range (0, element):
				starCount += "*"
			print starCount

x = [4,"Tom",1,"Michael",5,7, "Jimmy Smith"]
draw_stars(x)