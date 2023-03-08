#Write a Python program to copy the contents of a file to another file

with open("test.txt") as f:             #opened in f stream
    with open("out.txt", "w") as f1:    #opened with write mode
        for line in f:                  #reiterate with for loop
            f1.write(line)              #repited string copied in out file

f1 = open("out.txt", "r")
print(f1.read())