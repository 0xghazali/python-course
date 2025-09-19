# Step 1: Simple Function
def say_hello(): # def = keyword to define a function. say_hello = function name. () = no input right now.
    print("Hello, world!")

say_hello() # Inside: code runs when you call the function.
say_hello()

# Step 2: Function with Parameter
def greet(name): # name is a parameter (input to the function).
    print("Assalamualaikum", name)

greet("Ali") # When you call: greet("Ali") → name becomes "Ali".
greet("Sara") # When you call: greet("Sara") → name becomes "Sara".

# Step 3: Function with Return Value
def add(x, y):
    return x + y # return sends the result back.

result = add(5, 3) # add(5, 3) will give 8.
print("Sum is", result)

# Step 4: Functions Inside Functions (Combine)
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(2, 3))

# 👉 Functions can call other functions too.
# def → define function.
# () → pass inputs (parameters).
# return → give back a result.
# Functions help in reusability and clean code.
