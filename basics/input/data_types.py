#Here I will be trying out different data types

name = str(input("What is your name?"))
#String for names, names usually require letters
age = int(input("What is your age? "))
#integers are for integers numbers
height = float(input("How tall are you?(meters)"))
#Float is used for real numbers
weight = float(input("How much do you weigh(Kg)"))
bmi = float(weight/(height**2))
#Bmi is not an output, is just the input, so we just assign the data type
print(name,"you are",age,"and your bmi is {0:.2f}".format(bmi) )
#This will print every output
#The format function will print the result with 2 other decimals