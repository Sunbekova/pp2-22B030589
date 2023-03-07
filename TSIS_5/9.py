#Write a Python program 
#to insert spaces between words starting with capital letters.

import re

text = input()

def cap_w_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

print(cap_w_spaces(text))