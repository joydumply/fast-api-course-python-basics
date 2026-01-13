"""
Dictionaries
"""

user_dict = {
	"username": "nikfurylogin",
	'name': 'Nik',
	'age': 29
}

user_dict["married"] = True
user_dict.pop('age')
# user_dict.clear()

print(len(user_dict))
print(user_dict)
print(user_dict.get("username"))

for x, y in user_dict.items():
	print(x, y)

user_dict2 = user_dict #store pointer
user_dict2 = user_dict.copy() #create a copy