import re

text = input()
def func(text):
    matched = re.matched(r'ab*', text)
    if matched:
        return True
    return False

func(text)