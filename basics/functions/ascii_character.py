# Getting an ASCII CHARACTER

print("Pogram Started!")
print("Please enter an ASCII code.")

code = int(input())

if code in range (32,126):
  letter = chr(code)
  print("The character for the code {} is : {}".format(code,letter))
else:
  print("Wrong code pablo.")

print("Program Ended.")

  

  


