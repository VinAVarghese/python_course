# Simple cli app using .input() to read user input in python

print("How many Kilometers did you bike today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride is equal to {miles}mi")
