print "Long-long Vowels Exercise"
# Given a word as a string, print the result of extending any long vowels to the
# length of 5.

phrase = (raw_input("Enter a word or sentence: ")).lower()

new_phrase = ""
counter = 0

for letter in phrase:
    if counter == 2:
        counter = 0
        new_phrase += (match * 3)
    elif letter == "a" or letter == "e" or letter == "o":
        counter += 1
        match = letter
    new_phrase += letter

print new_phrase
