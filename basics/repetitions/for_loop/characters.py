# Making a program using user_strings

marks = str(input("What strange markings do you see?"))
print("Identifying...")
for count in range(0,len(marks),1):
  print("Index ",count, ":",end='')
  print(marks[count])
  
print("Done!")