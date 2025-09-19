# Step 1: Simple Dictionary
person = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

print(person)

# Step 2: Accessing Values
print(person["name"])
print(person["age"])

# Step 3: Adding / Updating Values
person["email"] = "ali@example.com"   # add new
person["age"] = 21                     # update existing
print(person)

# Step 4: Removing Values
del person["city"]
print(person)

# Step 5: Looping Through Dictionary
for key in person:
    print(key, ":", person[key])
