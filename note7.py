# Step 1: Using Built-in Module
import math

print(math.sqrt(16))   # square root
print(math.pi)         # value of pi

# Step 2: Import Specific Function
from math import sqrt, ceil

print(sqrt(25))    # 5.0
print(ceil(4.3))   # 5

# Step 3: Using Random Module
import random

print(random.randint(1, 10))   # random number between 1 and 10

# Step 4: Create Your Own Module
def greet(name): #create new file named mymodule.py
    print("Hello", name)

import mymodule # then create new file main.py and run this code

mymodule.greet("Ali")
