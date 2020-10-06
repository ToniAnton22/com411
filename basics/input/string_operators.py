#Creating a program using strings to make poor beep feel better

i = 0
lives = int(input("Insert the number of lives beep has "))
energy = int(input("Insert his energy level "))
shield = int(input("Insert his shielding capacity "))

print("Health has been set to: ",end = '')
#Tried not to use a Loop
#ended up using for anyway
#for i=0 in the range of lives
#for will add i++ until it matches the range (lives)
#then it will stop printing when i=lives

for i in range(lives):

  print ("♥",end = '')

print("\nEnergy has been set to: ",end = '')

for i in range(energy):

  print ("♠",end = '')

print("\nShield has been set to: ",end = '')

for i in range(shield):

  print ("♦",end = '')

  #I also used end = '' so I don't get a space
  #inbetween prints


