#There're 3 types of number:
#int
#float
#complex

x = 1
y = 3.14
z = 1j 
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 3.14
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#power of 10
#floats:
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# use j instead i. Like jmagine :D 
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#convert:

# !!!!
# u can't convert COMPLEX !-> int || float
# !!!!  

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#int -> float:
a = float(x)

#float -> int:
b = int(y)

#int -> complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#to call random() numbers
import random
print(random.randrange(1, 10))