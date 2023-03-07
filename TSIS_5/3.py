import re

text = input()
def funct(text):
    pattern = r'[a-z]+_[a-z]+'
    find = re.search(pattern, text)
    if find:
        return(find.string)
        


funct(text)
    