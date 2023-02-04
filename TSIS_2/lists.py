#ordered, indexed, changeable, have duplicates

#make list with help [ ]
my_list = ["U", "I", "We", "She", "U"]
print(my_list)

print(my_list[1])

my_list = sorted(my_list)
print(my_list)

print(my_list[1])

print(len(my_list))



l1 = ["a", "b", "c"]
print(l1)
#check type:
print(type(l1))

l2 = [1, 2, 3, 4, 5]
print(l2)
print(type(l2))

l3 = [True, False, False]
print(l3)
print(type(l3))


#list can contain any types of date:
list1 = ["a", 3,  True, 3.4, "AA AA"]
print(list1)
print(type(list1))

#type of list is <'list'>

#we can make list with: list((db, dfgb, grt))
my_list = list(("U", "I", "We", "She", "U"))
print(my_list)

#some method:


a = my_list.count("U")
print(a)
i = my_list.index("U") #return first apear of element
print(i) #starts with 0

my_List = [1, 2, 3]
my_list.append(my_List) #add my_List elements as 1 at the end
print(my_list)

my_list.extend(my_List) #add my_List element as independent from each other elements
print(my_list)

my_List.clear() #remove all elements
print(my_List)

x = my_list.copy()
print(x)
x.pop(5)
print(x)

my_list.insert(1, x) #insert as 1 element
print(my_list)

my_list.remove(my_List)
print(my_list)
my_list.remove(x)
my_list.reverse()
print(my_list)
