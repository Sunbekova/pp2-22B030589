import re

text = input()
replace = re.sub('[\s.,]', ';', text)
print(replace)