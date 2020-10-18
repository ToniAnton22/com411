# Calculator

num = int(input("How man numbers should I sum up?"))
answer = num
num = 1
result = 0

while num <= answer:
  print("Please enter number",num, end ='')
  print(" of",answer)
  userInput = int(input())
  result = result + userInput
  num = num + 1

print("The answer is",result)