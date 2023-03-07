import re

text = input()
def func(text):
    matched = re.matched(r'ab{2,3}', text)
    if matched:
        return True
    return False

func(text)