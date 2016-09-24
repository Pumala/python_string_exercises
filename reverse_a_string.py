print "Reverse a String Exercise"
# Prompt user for input and return the reversed form of their input

user_input = raw_input("Enter a word or sentence: ")
reversed_form = ""
length = len(user_input)
counter = 1

while len(reversed_form) != length:
    reversed_form += user_input[len(user_input) - counter]
    counter += 1

print reversed_form
