# Creating a program that prints emojies

rows = int(input("How many rows should I have?"))
columns = int(input("How many columns should I have?"))

print("Here I go")

for count in range(0,rows,1):
  for count in range(0,columns, 1):
    print(":)",end='')
  print()


print("Here are your emojies")