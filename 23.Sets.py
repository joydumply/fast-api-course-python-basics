"""
Sets are similar to lists but are unordered and cannot contain duplicates
"""
my_set = {1,2,3,4,5,1,2}

my_set.discard(3)
my_set.add(6)
my_set.update([7,8])
print(my_set)
