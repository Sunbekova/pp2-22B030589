#Write a Python program to delete file by specified path
#Before deleting check for access and whether a given path exists or not.

import os

filePath = 'some_path:))'

if os.path.exists(filePath):    #cheking path
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")