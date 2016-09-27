print "Caesar Decipher Exercise"
# Given a string that has been "ciphered", return the deciphered form

ciphered_text = "abobql pbhyq haqrefgnaq jul gur ghegyr pyvzorq bagb gur juvzfvpny qnapvat onex gung ynl arneyl sbetbggra va gur fhzzre urng"
shifted = 13

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
new_message = ""

for char in ciphered_text:
    for letter in alphabet:
        if char == letter:
            index = (alphabet.index(letter)) + shifted
            if index > 25:
                neg_index = (index - 25)
                index = neg_index - 1
            new_message += alphabet[index]
    if char == " ":
        new_message += " "

print new_message
