# Activity
# variables: first_name, last_name, age, DOB
# Prompt user to input above values
# Print/display the type of each value received from the user
# then display the data back to the user with greeting message
first_name = input("Please enter your first name: ")
last_name = input("...and now your last name: ")
age = input("...now your age: ")
date_of_birth = input("...finally, your date of birth: ")

print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(date_of_birth, type(date_of_birth))

print("To confirm, your name is: {} {}, you say you are {} years old and you were born on {}".format(first_name, last_name, age, date_of_birth))