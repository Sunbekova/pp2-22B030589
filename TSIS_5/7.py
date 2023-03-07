#Write a Python program to convert a given 
#camel case string to snake case.


import re

text = input()


def snake_to_camel(text):
    snake = re.findall(r'(\w+)_(\w+)', text)
    return re.sub(r'(\w+)_(\w+)', r'\1\2', text).capitalize()

print(snake_to_camel(text))

