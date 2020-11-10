# Creating a program that can determine the ASCII 
# code for characters

print("Porgram Started!")
print("Please enter a standard character: ")

letter = input()

if len(letter) == 1:
  value = ord(letter)
  
  print("The ASCII code for {} is: {}".format(letter, value))
else:
  print("Wrong format.")

print("Program has ended.")