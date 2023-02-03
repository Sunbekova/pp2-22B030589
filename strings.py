print("Hello")
print('Hello')
#no differense " & '

#variable 
a = "Hi"
print(a)

#multiline string
#use with triple " ->
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a)

#string - array
a = "Hello, World!"
print(a[1])

#loop through string:
for i in "banana":
    print(i)

#length
a = "Keep it up!"
print(len(a))

#cheaking elements:
s = "You can do it! I believe that it'll be easy for you!!!"
print("you" in s)
print("The" in s)
print('a' in s)


print("PP2" not in s)

#ex with if:
s = "You can do it! I believe that it'll be easy for you!!!"
if "you" in s:
    print("Yes, 'you' is present.")
if "The" in s:
    print("Yes, 'The' is present.")


if "The" not in s:
    print("No, 'The' is Not present.")

b = "Hello, World!"
print(b[2:7])
#form 2 to 5 char

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])