#Step 1 - Hello World
print("Hello World") #print() # means show something on the screen. "Hello World" is just text inside quotes.

#Step 2 - Taking input
name = input("Your Name: ") # input() asks the user to type something.Whatever user types → stored in a variable (name).
print("My Name is", name) # print() shows a message + the variable.

#Step 3 - Simple Math
x = 5 # x = 5 → variable x has number 5.
y = 10 # y = 3 → variable y has number 3.
print("x + y =", x + y) # + adds numbers.
print("x * y =", x * y) # * multiplies numbers.
print("x / y =", x / y) # / divides numbers.
print("x - y = ", x - y) # - subtracts numbers.

#Step 4 - File Handling
with open ("name.txt", "a") as f: # "a" = append, adds data without deleting old # open("filename", "mode") → opens a file.
    f.write("Ghazali\n") # write "Ghazali" + move to next line # with ... as f: → automatically closes file when finished. # f.write("Ali\n") → writes text into the file.

with open ("name.txt", "r") as f: # "r" = read #
    data = f.read() # read the full content # f.read() → reads everything from the file.
    print("File Content:\n ", data) # show it on screen # \n makes sure each entry goes to a new line.



