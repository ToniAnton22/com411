# Creating a program using a while loop to charge beep's batteries

line = int(input("How many bars should be charged?"))
maxLine = line
line = 0

while line >= 0 and line < maxLine:
  print("Charging: ",end='')
  line = line +1
  print('■'*line) 

print("Battery is fully charged")