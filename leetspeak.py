print "Leetspeak Exercise"
# Given a paragraph of text as a string, print the
# paragraph in leetspeak. To translate a string to
# leetspeak, you need to replace make the following
# character replacements (treat all input characters as
# uppercase):

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "p", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
            ]
user_string = raw_input("Enter a paragraph: ").upper()
leet_code = ""

for char in user_string:
    if char == "A":
        char = "4"
    elif char == "E":
        char = "3"
    elif char == "G":
        char = "6"
    elif char == "I":
        char = "1"
    elif char == "O":
        char = "0"
    elif char == "S":
        char = "5"
    elif char == "T":
        char = "7"
    else:
        pass
    leet_code += char

print leet_code

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7
