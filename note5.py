# Step 1: Simple List
fruits = ["apple", "banana", "mango"]
print(fruits)

# Step 2: Accessing Items
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # first item
print(fruits[1])   # second item
print(fruits[-1])  # last item reversing order

# Step 3: Adding Items
fruits = ["apple", "banana", "mango"]
fruits.append("orange")   # add at end
print(fruits)

# Step 4: Removing Items
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)

# Step 5: Looping Through List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("I like", fruit)
