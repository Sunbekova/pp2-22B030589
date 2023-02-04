#unordered, unindexed, no duplicate,
#unchangeable, but you can remove and/or add items

#create sets with { }:
my_set = {"U", "I", "We", "She", "U"}
#remove duplicates
print(my_set)
#return randomly placed elements
#can't call elements by index or e.t.c
print(len(my_set)) #will return # of exclusive elements

#contain str, int, boolean:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, False}
print(set1, set2, set3)

##can mix all of them:
my_set = {"asd", 3.4, True, 89, "AA AA"}
print(my_set, type(my_set))

#make set with -> set((fdg, ghj, 6)):
mySet = set(("PP2", 3.1415, True, 91, "Atack of Titan"))
print(mySet, type(mySet))