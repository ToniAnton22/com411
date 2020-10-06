#Learning the use of Modulo Operators
print("To check whether your number is odd or even, please insert a number here: ")
wholeNumber = int(input())

if wholeNumber % 2 == 0:
  print("Your number is even!")
elif wholeNumber % 2 != 0:
  print("Your number is odd")
else:
  print("Please insert a number next time.") 