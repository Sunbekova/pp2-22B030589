#Write a Python program to write a list to a file

items = list(input())
with open('items.txt','w') as file:
	file.write(''.join(items))
	
f1 = open('items.txt','r')
print(f1.read())
