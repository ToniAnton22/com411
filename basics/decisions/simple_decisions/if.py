#Define the global variable

nameBook = input("What type of book is this?")
book = "adventure"
#Create an if statement
if str(nameBook) == str(book):
  print("I like {} books!".format(nameBook))
#If the nameBook is equal to book
#then the "if" statement will print what's inside it 
print("Finished reading book.")
#the last print will be printed regardless of the "if"