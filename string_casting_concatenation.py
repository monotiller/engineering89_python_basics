single_quotes = 'These are single quotes and are working perfectly fine'
double_quotes = "These are double quotes and are working perfectly fine"

print(single_quotes) # = These are single quotes and are working perfectly fine
print(double_quotes) # = These are double quotes and are working perfectly fine
print(single_quotes+ ' ' + double_quotes)

First_Name = "Joe"
Last_Name = "Bloggs"
Age = 56
print(First_Name + ' ' + Last_Name + '. And your age is: ' + str(Age))

greetings = "Hello World!"
print(len(greetings))
print(greetings[0:5])
print(greetings[-1])
print(greetings[6:])
print(greetings[-6:])

white_spaces = "Lot's of white spaces                    "
print(len(white_spaces))
print(white_spaces.strip())
print(len(white_spaces.strip()))

example_text = "here's some text with lot's of text"
print(example_text.count("text"))

print(example_text.upper())
print(example_text.lower())
print(example_text.capitalize())
print(example_text.replace("with", ","))