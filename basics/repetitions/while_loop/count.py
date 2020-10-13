# Demonstrating while loops
cables = int(input("How many cables should I remove?"))

while cables > 0 and cables <= 10:
   print("Removing {} cables".format(cables))
   cables = cables + 1
