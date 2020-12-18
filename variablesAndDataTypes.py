# Note: No "let"/"var"/"const" like JS used.
# Python is dynamic like JS where data type does NOT need to be defined when creating the variable

x = 100
khalessi_mother_of_dragons = 1
print(khalessi_mother_of_dragons + x) # 101

# Python Naming convention
    # "snake_case" used over "camelCase"
    # Constants are in all caps e.g. "SNAKE_CASE"
    # "duner" used to explicitally say not to touch a variable i.e. "_snake_case_"

# Unique Python Data Types (in comparison to JS)
    # Booleans must start with a capital for Python to recognize it as a Boolean
test_boolean = True
print(test_boolean)
    # List = Array
    # Dictionaries = Object i.e. a collection of key: values
example_dict = {"first_name":"Vin", "last_name":"Vargh"}
print(example_dict)

# None = null
    # MUST use capital 'N' as "none" would be considered to be an assignable variable name by python

# Interpolating using the "f string"
    # Add an f before your string and use curly braces where you want to inject a variable
guess = 8
print(f"your guess of {guess} was incorrect!") # your guess of 8 was incorrect!

# Converting Data Types
    # use the name of the builtin type as a function
decimal = 12.56345634534
integer = int(decimal) #(float changed to a int by being floored)
print(integer) # 12 

integer = 8
string = str(integer)
print(string, type(string))

