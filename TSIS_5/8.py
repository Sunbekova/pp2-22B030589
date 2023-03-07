#Write a Python program to split a string at uppercase letters.
import re

text = input()
matches = re.findall("[A-Z][^A-z]*", text)
print(matches)

