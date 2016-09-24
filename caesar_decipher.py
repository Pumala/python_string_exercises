print "Caesar Cipher Exercise"
# Given a string that has been "ciphered", return the deciphered form

ciphered_text = "xibu ep zpv uijol bcpvu uif tlz"

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
deciphered_text = ""

for letter in ciphered_text:
    for alpha in alphabet:
        if letter == alpha:
            index = (alphabet.index(alpha)) - 1
            deciphered_text += alphabet[index]
    if letter == " ":
        deciphered_text += " "

print deciphered_text
