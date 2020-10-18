# Calculating factorial numbers with while

num= int(input("Please enter a number: "))
result = int()
factorial = 1
while num > 1:
  result = num *(num-1)
  num = num - 2
  factorial = result * factorial

print("The factorial is ",factorial)