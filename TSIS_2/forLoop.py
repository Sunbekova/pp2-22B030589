n = str(input())
for i in n:
    print(i)

for x in "banana":
    print(x)

arr = [1, 2, 3, 0, 4, 5, 6, 7]
for x in arr:
    print(x)
    if x==0: #stop loop after 0
        break

arr = [1, 2, 3, 0, 4, 5, 6, 7]
for x in arr:
    if x==0: #stop loop before 0
        break
    print(x)

arr = [1, 2, 3, 0, 4, 5, 6, 7]
for x in arr:
    if x==0: #jump over 0
        continue
    print(x)

#range()
for x in range(6):
    print(x) #starts from 0 till 5 = 6 numbers

for x in range(2, 6):
    print(x) # starts from 2 till 5

for x in range(5, 46, 3):
    print(x) #starts from 5 till 45 and x +=3



for x in range(6):
  print(x)
else: # else won't work if code stops with break
  print("Finally finished!")


for x in range(6):
    if x == 3: break
    print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in 1000:
    pass
