"""
Q) 1)
myStr = input("Enter your name: ")
print("Good afternoon " + myStr)

"""
"""
Q) 2)
name = input("Enter your name: ")
date = input("Enter the date: ")

template = '''Dear <|Name|>, 
your are selected !
<|Date|>
'''
print(template.replace("<|Name|>", name).replace("<|Date|>", date))
"""

"""
Q) 3) In this question we are finding where Double spaces are found
myStr = "This is Siva  saikumar reddy"
print(myStr.find("  "))
"""

"""
Q) 4) Replace the double space with single space.
myStr = "This is Siva  saikumar reddy"
print(myStr.replace("  ", " "))

"""

"""
Q) 5) write a program to format the following letter using escape Sequence characters
letter = "Dear Sivasai, \n\tWe are happy to inform that you have been selected to Google. \nThanks!"
print(letter)
"""