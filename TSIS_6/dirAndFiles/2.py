#Write a Python program to check for access to a specified path
#Test the existence, readability, writability and executability of the specified path

import os

path = 'c:\\Users\\suanb\\Desktop\\PP_2\\TSIS_6\\dirAndFiles\\E.txt'

print('Exist:', os.access(path, os.F_OK)) #os.F_OK func fo checking path

print('Readable:', os.access(path, os.R_OK))#os.R_OK func check readable

print('Writable:', os.access(path, os.W_OK))#os.W_OK func check writable

print('Executable:', os.access(path, os.X_OK))#func check executable
