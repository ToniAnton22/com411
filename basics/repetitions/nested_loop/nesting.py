# Creating a program
# Which would print an X on different positions
# Based on user input 


print("Please enter a sequence:")
sequence = input()

print("Please enter the character for the marker: ")
marker = input()

# Find markers
position1 = -1
position2 = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]

    if (letter == marker):
        if (position1 == -1):
            position1 = position
        else:
            position2 = position

# Display result
print("The distance between the markers is ", position2 - position1 - 1)

    
