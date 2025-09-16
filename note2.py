# Step 1: Simple If
x = 10 # variable given with value
if x > 5: # if checks a condition (here: x > 5).
    print("x is greater than 5") # screen output

# Step 2: If + Else

age = int(input("Enter your age: ")) # taking input
if age >= 18: # >= means “greater than or equal to”. # If condition is True → run first block.
        print("You are a adult")
else: # Else → run the second block.
        print("You are a minor")

# Step 3: If / Elif / Else
marks = int(input("Enter your marks: ")) # Python runs from top to bottom:
if marks >= 80: # If first condition is True → stop there.
    print("Grade A")
elif marks >= 60: # elif = “else if”, checks the next condition.
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else: # else = if none of the conditions are True.
    print("Grade D")
