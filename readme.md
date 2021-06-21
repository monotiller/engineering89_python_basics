
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
### Activity
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

## Data types and operators
What are data types and operators?

Data types are the core of all programming languages. After all, if there is no data there is not a program.

Through the next few lessons we will be learning about all many of the data types available and more importantly some of the inbuilt methods around these data types that we can guarantee will be valuable to you as you progress.

Some data types:
- Boolean (True or false)
- Numbers (Integers, double, float, longs)
- Strings (Text)
- Operators (See tables below)
### Arithmetic Operators
| Operand    | Description                          | Example    |
|:---------: |:----------------------------:        |:--------:  |
|    +       | add two operands (variables) together| X + y + 2  |
|    -       | subtract two operands (variables)    | X - y - 2  |
|    *       | multiply two operands (variables)    | X - y - 2  |
|    /       | divide two operands (variables)      | X - y - 2  |
|    %   | Modulus - remainder of the division of left operand by the right    | X - y - 2  |
|    +       | add two operands (variables) together| X + y + 2  |
|    **       | does powers of                      | X ** y  |

### Comparison Operators
| Operand    | Description                          | Example         |
|:---------: |:----------------------------:        |:--------:       |
|    >       | True if left operand is greater than the right| x > y  |
|    <       | True if left operand is less than the right| x < y     |
|    ==      | True if both operands are equal            | x == y    |
|    !=      | True if both operands are equal            | x != y    |
|    >=      | True if left operand is greater than or equal to the right| x >= y     |
|    <=      | True if left operand is less than or equal to the right| x <= y     |

### Examples
```python
number_1 = 4
number_2 = 2

print(number_1 + number_2) # Adding two values = 6
print(number_1 - number_2) # Subtracting two values = 2
print(number_1 * number_2) # Multiplying two values = 8
print(number_1 / number_2) # Dividing two values = 2.0 (because division immediately turns this in to a float)
print(number_1 % number_2) # Remainder of two values = 0
print(number_1 ** number_2) # Power of a number so 4^2 = 16
```

Let's look at boolean values
```python
number_1 = 4
number_2 = 2

print(number_1 == number_2) # is number_1 equal number_2 = False they are not equal
print(number_1 != number_2) # is number_1 not equal to number_2 = True they are not equal
print(number_1 >= number_2) # is number_1 greater than number_2 = True
print(number_1 <= number_2) # is number_1 less than number_2 = False
```
