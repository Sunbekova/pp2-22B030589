#arithmetic operators:
x = 10
y = 2
print(x+y)
print(x - y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

#assignment:
x=5
x+=3 #x = x+3
print(x)

x = 5
x-=3 #x = x-3
print(x)

x = 5
x*=3 #x = x*3
print(x)

x = 5
x/=3 #x = x/3
print(x)

x = 5
x%=3 #x = x%3
print(x)

x = 5
x//=3 #x = x//3
print(x)

x = 5
x**=3 #x = x**3
print(x)

x = 5
x &=3 #x = x&3
print(x)

x = 5
x |=3 #x = x|3
print(x)

x = 5
x ^=3 #x = x^3
print(x)

x = 5
x>>=3 #x = x>>3
print(x)

x = 5
x<<=3 #x = x<<3
print(x)

#logical:
print(3<5 and 3<10)
print(6<5 or 6<10)
print(not(3<5 and 3<10))

#idintification:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, 
# even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, 
# even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y


#membership:
x = "The string"
print("string" in x)
print("string" not in x)
print("fgh" not in x)


#bitwise:

print(6&3)
# & multiply bitstrings of 6 and 3
print(6|3)
# | add bitstrings of 6 and 3
print(6^3)
# ^ compares each bit and 1 if and only if 1+0
print(~3)
# ~ inverse all bits
print(3<<2)
# << shift bits by 2 steps left
print(8>>3)
# >> shift bits by 3 steps right 
