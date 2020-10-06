first_number=int(input("Insert first whole number "))
print(first_number)
second_number=int(input("Insert second whole number "))
print(second_number)
third_number=int(input("Insert third whole number "))
print(third_number)


if first_number%2 != 0:
  if (second_number* third_number)%2 != 0:
    print("There are 3 odd numbers.")
  elif second_number%2 == 0:
    if third_number%2 != 0:
      print("There are 1 even numbers and 2 odd one!")
    elif third_number%2 == 0:
      print("There are 2 even number and 1 odd number.")  
  elif second_number%2 != 0:
    if third_number%2 == 0:
      print("There are 2 odd numbers and 1 even number.")  
elif first_number%2 ==0:
  if (second_number* third_number)%2 != 0:
    print("There are 2 odd and 1 even numbers.")
  elif second_number%2 == 0:
    if third_number%2 != 0:
      print("There are 2 even numbers and 1 odd one!")
    elif third_number%2 == 0:
      print("There are 3 even numbers.")  
  elif second_number%2 != 0:
    if third_number%2 == 0:
      print("There are 1 odd numbers and 2 even number.")  
