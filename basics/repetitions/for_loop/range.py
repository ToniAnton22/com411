# Playing around with beep's brightness 

lvl = int(input("What level of brightness is required?(chose an even number)"))
hiddelvl= int()
print("Adusting Brightness....")
lvl = lvl +1
for count in range(2,lvl,2):

  print("Beep's Brightness level: ",end='')
  print('*'*count)
  print("Bop's brightness level: ",end='')
  print('*'*count)
  
  
print("Adjustments complete!")