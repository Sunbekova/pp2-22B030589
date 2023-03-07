import re

text = input()

matches = re.match(r'a.*b', text)
if matches:
    print(matches.string)
else: print('Noting')