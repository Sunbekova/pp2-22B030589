#example of types:
x = "Hello World"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))		
x = ("apple", "banana", "cherry")
print(type(x))		
x = range(6)
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))	
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))	
x = True
print(type(x))		
x = b"Hello"
print(type(x))		
x = bytearray(5)
print(type(x))	
x = memoryview(bytes(5))
print(type(x))	
x = None
print(type(x))

#appropriation data type:
y = str("Hello World")
print(type(y))	
y = int(20)
print(type(y))
y = float(20.5)
print(type(y))	
y = complex(1j)	
print(type(y))	
y = list(("apple", "banana", "cherry"))
print(type(y))	
y = tuple(("apple", "banana", "cherry"))
print(type(y))	
y = range(6)
print(type(y))	
y = dict(name="John", age=36)
print(type(y))	
y = set(("apple", "banana", "cherry"))
print(type(y))
y = frozenset(("apple", "banana", "cherry"))
print(type(y))	
y = bool(5)
print(type(y))	
y = bytes(5)
print(type(y))	
y = bytearray(5)
print(type(y))	
y = memoryview(bytes(5))
print(type(y))