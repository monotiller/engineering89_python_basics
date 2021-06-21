# Let's test the installation and environment
print("Hello Maddie")

# Variable? Just what are variables?
# print function is used to display outcome
# Python variables
# Variable works as a placeholder to store data
# It could be string "anything between these two quotation marks", you may also use these: '
# Integers/numbers
# Syntax to create a variable: name_of_variable = value
# Follow good logical naming convention

First_Name = "Maddie"
Last_Name = "Marsh"
# Let's create a variable to store int value
Salary = 10.5 # Float value
age = 19  # Int value
my_age = "24"

print(First_Name)
print(Last_Name)
print(Salary)
print(age)
print(my_age) # How do we know that this is a string ang not an integer?

# type() helps us find the type of variable
print(type(age)) # Will print the type of variable age = <class 'int'>
print(type(my_age)) # Will print the type of variable my_age = <class 'str'>

# input() in python to interact with user - to ask user to enter required data
print(input("Please enter your name: ")) # This will just print out exactly what the user enters

# But we can store that variable!
User_Name = input("Please enter your name: ")
print("Hello")
print(User_Name)

# Activity
# variables: first_name, last_name, age, DOB
# Prompt user to input above values
# Print/display the type of each value received from the user
# then display the data back to the user with greeting message