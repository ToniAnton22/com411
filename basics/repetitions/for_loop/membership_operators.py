# Reversing words in for loops

phrase = str(input("What phrase do you see?"))

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed) 

print("Reversing...")

print("The phrase is: ",phrase)
