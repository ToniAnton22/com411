#Classifying books using their cover
#Ask user about the type of cover
cover = input("Enter your cover type (Hard/soft): ")

# create if
if cover == 'soft':
  # ask user about the "perfect bound"
  typeBook = input("Is your book perfect bound (yes/no)?")

  if typeBook =='yes' or typeBook == 'Yes':
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books!")
elif cover == 'hard':
  print("Books with hard covers can be more expensive.")
else:
  print("I don't know what's that.")  

    


  
