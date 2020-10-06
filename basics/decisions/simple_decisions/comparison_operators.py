#comparison operators by being able to identify the smallest of two numbers.

first_number= int(input("Please insert your first number: "))
print("Your first number is: ", first_number)
second_number = int(input("Please enter your second number: "))
print("Your second number is: ", second_number)

if first_number > second_number:
  print("Your first number is bigger than your second number.")
elif first_number < second_number:
  print("Your second number is bigger than your first number.")
elif first_number == second_number:
  print("Your numbers are equal.")
else:
  print("Please enter numbers next time.")