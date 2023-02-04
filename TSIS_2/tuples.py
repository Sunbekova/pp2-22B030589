#ordered, indexed, have duplicates, 
#unchangeble - cannot add/remove items after creation tuple

#tuple initialize with ( )
my_tuple = ("U", "I", "We", "She", "U")
print(my_tuple)
print(my_tuple[3])#index starts with 0
print(len(my_tuple))

#if u want create tuple with 1 elem, put coma:
my_tuple = ("tuple",) #type -> tuple
print(type(my_tuple))

not_tuple = ("tuple")
print(type(not_tuple)) #type -> str


#contain str, int, boolean:
t1 = ("a", "b", "c")
t2 = (1, 2, 3, 4, 5)
t3 = (True, False, False)
print(t1, t2, t3)
print(type(t1), type(t2), type(t3))
#can mix all of them:
tuple1 = ("asd", 3.4, True, 89, "AA AA")
print(tuple1, type(tuple1))

#make tuple with -> tuple((fg, hj, 6))
my_tuple = tuple(("PP2", 3.1415, True, 91, "Atack of Titan"))
print(my_tuple, type(my_tuple))