#Write a Python program to list only directories,
#files and all directories, files in a specified path.

import os

#os.listdir() will list all files and directories.
#os.path.isdir() if it is a directory it will return true.

path = 'c:\\Users\\suanb\\Desktop\\PP_2\\TSIS_6\\dirAndFiles'

print("Only directories:")
p1=os.listdir(path)
for i in p1:
    if os.path.isdir(i):
        print(i)

print("\nOnly files:")
for i in p1:
    if not os.path.isdir(i):
        print(i)

print("\nAll directories and files :")
for i in p1:
    print(i)