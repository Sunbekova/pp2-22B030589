# if we have input from terminal
# and we need include it to our string use:
price = int(input())
string = "The price is {} dollars"
print(string.format(price))
#it makes price into str, as i understood

#also we can give some parametrs in format():
string = "The price is {:.2f} dollars" #some number.00
print(string.format(price)) 

thing = str(input())
price = int(input())
order = "I want {} for {:.3f} dollars"
print(order.format(thing, price))

#use indexes:
quantity = 3
itemno = 567
price = 49
order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(order.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#{name} and print through given info for {}
info = "My name is {name}, I'm {age} years old"
print(info.format(name = "Aisha", age = "17"))