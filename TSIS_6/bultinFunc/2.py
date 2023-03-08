#Write a Python program with builtin function that accepts a string
#and calculate the number of upper case letters and lower case letters

str = input()
low_case = 0
up_case = 0

for i in str:
    if  ord(i) >= 65 and 90 >= ord(i):
        low_case += 1
    elif ord(i) >= 97 and 122 >= ord(i):
        up_case += 1

print(low_case, up_case)