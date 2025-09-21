# Step 1: Writing CSV File
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ali", 20, "Karachi"])
    writer.writerow(["Sara", 22, "Lahore"])

# Step 2: Reading CSV File
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Step 3: Reading CSV as Dictionary
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], "-", row["City"])
