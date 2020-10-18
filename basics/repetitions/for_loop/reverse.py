# Reversing words in for loops

phrase = str(input("What phrase do you see?"))

for count in range(len(phrase)-1,-1, -1):
  print(phrase[count])
 

print("Reversing...")

print("The phrase is: ",phrase)
