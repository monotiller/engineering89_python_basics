# Python
## Why python?
### Python installation and Pycharm setup

- Test installation and pycharm
- Python is a dynamically typed language

Let's test the installation and environment
```python
print("Hello Maddie")
```
## Variable? Just what are variables? 
- `print` function is used to display outcome
- Variables work as a placeholder to store data
- It could be string `"anything between these two quotation marks"`, you may also use these: `'`
- Integers/numbers
- Syntax to create a variable: name_of_variable = value
- Follow good logical naming convention
```python
First_Name = "Maddie"
Last_Name = "Marsh"
```
Let's create a variable to store int value
```python
Salary = 10.5 # Float value
age = 19  # Int value
my_age = "24"

print(First_Name)
print(Last_Name)
print(Salary)
print(age)
print(my_age)
```
How do we know that this is a string ang not an integer? type() helps us find the type of variable

```python
print(type(age)) # Will print the type of variable age = <class 'int'>
print(type(my_age)) # Will print the type of variable my_age = <class 'str'>
```
`input()` in python to interact with user - to ask user to enter required data
```python
print(input("Please enter your name: ")) # This will just print out exactly what the user enters
```
But we can store that variable!
```python
User_Name = input("Please enter your name: ")
print("Hello")
print(User_Name)
```
## Activity
- variables: `first_name`, `last_name`, `age`, `DOB`
- Prompt user to input above values
- Print/display the type of each value received from the user
- then display the data back to the user with greeting message
```python
first_name = input("Please enter your first name: ")
last_name = input("...and now your last name: ")
age = input("...now your age: ")
date_of_birth = input("...finally, your date of birth: ")

print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(date_of_birth, type(date_of_birth))

print("To confirm, your name is: {} {}, you say you are {} years old and you were born on {}".format(first_name, last_name, age, date_of_birth))
```