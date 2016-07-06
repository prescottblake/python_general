import random
import datetime
start_time = datetime.datetime.now()
randNumList = []
for i in range (0,100):
	randNumList.append(int((random.random()*100)))

numList = [3,1,2]

def insertionSort(numList):
	for i in range (1, len(numList)):
		current = numList[i]
		index = i
		while index > 0 and numList[index -1] > current:
			numList[index]= numList[index-1]
			index = index-1
		numList[index] = current	
	print numList
insertionSort(randNumList)			
print "Elapsed Time: " +str(datetime.datetime.now() - start_time)			

#parse up through 
# index inital correct
# if selected value is less than the indexed element, move left
# else, plop it down