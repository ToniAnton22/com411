#The program will let the user enter their health, mana and shield
#and then draw an avatar picture of the avatar
hp = int(input("Please give us his hit points: "))
mana  = int(input("Please give us his mana pool: "))
shield = int(input("Please give us his shields: "))
stamina = 100
name = str(input("Please name your character: "))
#Now that the program can see it
#We need to make visible for the user using print
print("HP: ",'♥' *hp, end='')
print("\t\t\t\t\t\t\t\t\t\tShield",'◙'*shield)
print("Mana: ",'■' *mana, end='')
print("\t\t\t\t\t\t\t\t\t\tStamina",stamina)

print("\n\t\t\t\t\t\t",name)

print("\n\t\t===============================")
print("\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t●\b\t\t\t●\b\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t(------------)\b\b\b\b\b\b\b\b\b\b\b\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |\n\t\t|\t\t\t\t\t\t\t  |")
print("\t\t===============================")

#Last step, drawing the character.
#The middle print looks like a mess, but it proves that
#I know how to use escape characters properly
#I promise my next code won't look like that
