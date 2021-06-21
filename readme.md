
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

## String casting and concatenation
- Using and managing strings
- String casting
- String concatenation
- Casting methods
- Single *AND* double quotes

```python
single_quotes = 'These are single quotes and are working perfectly fine'
double_quotes = "These are double quotes and are working perfectly fine"

print(single_quotes) # = These are single quotes and are working perfectly fine
print(double_quotes) # = These are double quotes and are working perfectly fine
```
Don't forget, you can use the \ as an escape character so you may use either the single quote in a single quote or a double quote in a double!
### Concatenation
```python
print(single_quotes+ ' ' + double_quotes) # = These are single quotes and are working perfectly fine These are double quotes and are working perfectly fine
```
Concatenation allows you to literally add two strings together
```python
First_Name = "Joe"
Last_Name = "Bloggs"
print(First_Name + ' ' + Last_Name) # = Joe Bloggs
```
Now let's create a variable called `Age` and add it to the same line as `Joe Bloggs`
```python
First_Name = "Joe"
Last_Name = "Bloggs"
Age = 56
print(First_Name + ' ' + Last_Name + '. And your age is:' + Age)
```
Now this won't work. Why? Well because you can't concatonate anything that ***ISN'T*** a string:
```commandline
Traceback (most recent call last):
  File "/Users/monotiller/Developer/Sparta Global/python_engineering89_basics/string_casting_concatenation.py", line 11, in <module>
    print(First_Name + ' ' + Last_Name + '. And your age is:' + Age)
TypeError: can only concatenate str (not "int") to str
```
So, we can fix this by wrapping `Age` in `str()`:
```python
First_Name = "Joe"
Last_Name = "Bloggs"
Age = 56
print(First_Name + ' ' + Last_Name + '. And your age is: ' + str(Age))
```
Which gives us:
```commandline
"Joe Bloggs. And your age is: 56"
```

### String slicing
```python
greetings = "Hello World!"
```
In python (as many languages) counting starts at 0. So value `0` is `H`, `3` is `l`

To confirm the length of a string:
```python
len(greetings) # = 12
```
Now, let's slice:
```python
print(greetings[0:5]) # = Hello
```
So `0:5` means that it will print values 0 to 4, the last number is not included.

How do you reverse a string? Well, to get the last value of a string you just need to use `-1`
```python
print(greetings[-1]) # = !
```
This will slice the string right to left starting at `-1`

Now here's how you print only `World`
```python
print(greetings[6:]) # = World!
print(greetings[-6:]) # = World
```

### String built in methods
So, how do we remove data that isn't useful to us such as white spaces?
```python
white_spaces = "Lot's of white spaces                    "
```
We don't need the white spaces, but the enterpreter will see them
```python
print(len(white_spaces)) # = 41
```
We don't want the 41 characters. So we can use the `strip()` method. This will remove white spaces
```python
print(white_spaces.strip()) # = Lot's of white spaces
```
Let's check the length:
```python
print(len(white_spaces.strip())) # = 21
```

### Some more built in methods that we can use with string
How do we see how many times a word appears in a string? We use `count()`
```python
example_text = "here's some text with lot's of text"
print(example_text.count("text")) # = 2
```
This shows that there are 2 instances of `"text"` in `example_text`. But it is case sensitive, this is where `upper()` and `lower()` come  in to play. This makes it so that strings are forced into upper or lower case respectively
```python
print(example_text.upper()) # = HERE'S SOME TEXT WITH LOT'S OF TEXT
print(example_text.lower()) # = here's some text with lot's of text
print(example_text.capitalize()) # = Here's some text with lot's of text
```
We can also use `replace()` to, well, replace
```python
print(example_text.replace("with", ",")) # = here's some text , lot's of text
```