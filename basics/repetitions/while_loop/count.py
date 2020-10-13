# Demonstrating while loops
cables = int(input("How many live cables should I avoid?"))
liveCables = cables
cables = 0
while cables != liveCables :
  print("Avoiding....")
  cables = cables + 1
  print("Done! {} live cables has been avoided".format(cables))

print ("All live cables have been avoided.")
