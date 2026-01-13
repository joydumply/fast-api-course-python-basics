"""
Boolean and Operators
"""

like_coffee = True
like_tea = False

favorite_food = "Pizza"
favorite_number = 32

print(type(like_coffee))
print(type(like_tea))
print(type(favorite_food))
print(type(favorite_number))

print(1 == 2) #False
print(1 != 2) #True
print(1 >= 2) #False
print(1 <= 2) #True


print( 1 > 3 and 5 < 7) #and like &&
print( 1 > 3 or 5 < 7) #or like ||
print( not(1 == 1)) #not() like !