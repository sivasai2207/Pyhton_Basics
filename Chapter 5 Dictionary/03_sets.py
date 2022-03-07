mySet = {1, 3, 2, 5}
# Adding values to a existing set
mySet.add(27)
print(mySet)
# Adding a string to a set
mySet.add("2")
print(mySet)
# Using .Remove method to remove a specific value
mySet.remove("2")
print(mySet,"Removed")
# It is used to remove the value at random and prints the value back which has removed
print(mySet.pop())
print(mySet)

# To find the lenght of the set
print(len(mySet))