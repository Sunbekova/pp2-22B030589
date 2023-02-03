a = int(input())
b = int(input())
if a>b:
    print("a greater")

elif a<b:
    print("b greater")

else:
    print("a == b")

a = str(input())
b = str(input())
if len(a) > len(b): print(a , "is greater")
print(a) if len(a)>len(b) else print(b) #ternary op or conditional expression
print(a) if len(a)> len(b) else print("=") if len(a)==len(b) else print(b)

a = int(input())
b = int(input())
c = int(input())
if a>b and c>a:
    print("True")

elif a>b or a>c:
    print("At least 1 true")

elif not a>b:
    print("a is Not greater than b")




x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



a = 33
b = 200

if b > a:
  pass