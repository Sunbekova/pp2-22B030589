import re

text = input()
def func(text):
    pattern = r'[A-Z]{1}[a-z]+'
    find = re.findall(pattern, text)
    if find:
        print(find)
    else: print('Nothing')
    

func(text)