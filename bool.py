print(10>9)
print('a'=='b')
print(10<2)

a = 200
b = 33
if b>a:
    print("b ps greater than a")
else:
    print("a greater than b")

print(bool("11234"))
print(bool("Hello"))
print(bool(15))

x = "asd"
y = 8
print(bool(x))
print(bool(y))

#empty ones return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#method _len_ from class will return False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())


#function and using bool:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#check type and return bool:
x = 200
print(isinstance(x, int))
print(isinstance(x, str))