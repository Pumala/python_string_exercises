print "Caesar Cipher Exercise"
# Given a string, print the Caesar Cipher (or ROT13) of that string.
# What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

user_input = (raw_input("Enter a word or sentence: ")).lower()
shifted = int(raw_input("How many times would you like to shift the letter? "))

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
new_message = ""

for letter in user_input:
    for alpha in alphabet:
        if letter == alpha:
            index = (alphabet.index(alpha)) + shifted
            if index > 25:
                neg_index = (index - 25)
                index = neg_index - 1
            new_message += alphabet[index]
    if letter == " ":
        new_message += " "

print new_message
