myDict = {
    "Hi" : "Hi",
    "Yella Vunnaru": "How are you"
}
key = input("Enter they word: ")
if(myDict.get(key) == None):
    print("The entered Value not found")
else:
    print("The meaning of " + key + " is:", myDict.get(key))