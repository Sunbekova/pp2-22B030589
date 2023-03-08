#Write a Python program to generate 26 text files
#named A.txt, B.txt, and so on up to Z.txt

for i in range(65, 99):
    with open(chr(i)+".txt",'w') as file:
        file.write(chr(i))
