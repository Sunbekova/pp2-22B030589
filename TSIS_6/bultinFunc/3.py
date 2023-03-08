#Write a Python program with builtin function 
#that checks whether a passed string is palindrome or not.

str = input()

if str == str[::-1]: print('Polindrome')
else: print('No')