# Simple cli apps using .input() to read user input in python
# Practices conditional logic in python

age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    elif age >= 21:
        print("You can enter and drink")
    else:
        print("You cannot enter")
else:
    print("Please enter your age.")