# Step 1: For Loop (counting)
for j in range(10):  # for repeats code - range(5) means numbers from 0 → 4 (5 numbers total).
    print("Hello", j)  # Each time, i takes the next number.

# Step 2: Loop through a list
names = ["Ali", "Sara", "John"]  # A list is a collection of items (["Ali", "Sara", "John"]).

for z in names:  # for n in names: goes through each item one by one.
    print("Hello", z)  # n = "Ali", then n = "Sara", then n = "John".

# Step 3: While Loop
count = 2  # Start with count = 1.

while count <=10:  # while repeats as long as the condition is True - When count becomes 6, condition is False → loop stops.
    print("Count is", count)  #
    count = count + 2  # After each run, increase count by 1.

# Step 4: Breaking a loop
while True: # while True: = infinite loop (never stops by itself).
    text = input("Type 'exit' to stop: ")
    if text == "exit": # If user types "exit", we use break to stop the loop.
        break
    print("You typed:", text) # Otherwise it keeps repeating.
