# IF statements in Python
    # Syntax: if, elif, else, :, indentation
    # Note - white space sensitive
        #Error without indentation of condition's action
        #indentation is customarily 4 spaces (tab)
    #Format
        #if <condition>:
            #<action>
        #elif <alt condition>:
            #<action>
        #else:
            #<action>

#Example:
name = "Vinny"
# name = "Holli"
# name = "Sam"

if name == "Vinny":
    print("Welcome back Vin")
elif name == "Holli":
    print("Hi Holli")
else:
    print("User not recognized")

# "is" can be used to check truthiness
print(name is "Vinny") #True
print(name is "Blanka") #False
# "is" checks for place in memory while "==" checks value
x = 13
y = 13
x == y # True
x is y # True
a = [1,2]
b = [1,2]
a == b # True
a is b # False  
clone = a
a is clone # True

# python /===/ javaScript
# "and"   === &&
# "or"    === ||
# "not"   === !

age = 31 # "That's not your age"

if name is "Vinny" and age is 30:
    print("this is true")
elif name is "Vinny" and age is not 30:
    print("That's not your age")
else:
    print("Who are you?")


