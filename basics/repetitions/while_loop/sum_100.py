# Creating a calculator using while

print("Calculating the sum of the first 100 numbers...")
number = 0
result = int()
while number >= 0 and number <= 100:
  result = result + number
  number = number + 1


print("The sum is ", result)