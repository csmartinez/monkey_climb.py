# Gather information
print("Wondering how long it takes your monkey to reach the top of a tree? \nWell worry no longer! Welcome to Monkey Climb!") 
top = input("Enter tree height in feet: ")
height = input("Enter monkey's reach from the ground, in feet: ")
rate_of_climb = input("In 1 minute, how many feet can your monkey climb? ")
minute = 0

# Optional field - starting minute
# minute = input("Enter starting minute (ex 0): ")

# Loop through until top is reached, document monkey climb, output success at the end

while int(height) < int(top):
    height = int(height) + int(rate_of_climb)
    minute = int(minute) + 1
    if int(rate_of_climb) >= 1 and int(top) <= 120:
        print(str(height) + (" ft at minute " + str(minute)))
    else:
        print("Sorry, you entered invalid values to compute.")
        break
        
if int(height) == int(top) or int(height) > int(top):
    print("Conquered a " + str(height) + " ft tree in " + str(minute) + " minutes!")
