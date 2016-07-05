# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]



# def namePrint(students):
# 	for data in students:
# 		print data["first_name"], data["last_name"]


# namePrint(students)

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def namePrint(users):
	for key, category in users.items():
		count = 0
		print key
		for data in category:
			count += 1
			totalLength = len(data["first_name"]) + len(data["last_name"])
			print str(count), "-", data["first_name"], data["last_name"], "-", str(totalLength)

namePrint(users)