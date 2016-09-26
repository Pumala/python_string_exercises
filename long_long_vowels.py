print "Long-long Vowels Exercise"
# Given a word as a string, print the result of any 2 vowels in a row
# to the length of 5 instead

phrase = (raw_input("Enter a word or sentence: ")).lower()

new_phrase = ""
counter = 0

for letter in phrase:
    if letter == "a" or letter == "e" or letter == "o":
        counter += 1
        vowel = letter
        if counter == 2:
            counter = 0
            new_phrase += (vowel * 3)
    else:
        pass
    new_phrase += letter

print new_phrase
