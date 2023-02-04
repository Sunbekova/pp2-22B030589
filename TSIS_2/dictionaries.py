#ordered, changeable, no duplicate

#dictionaries open with { and have "key":"values"}:
my_dct = {
    "type": "Clothes",
    "material": "Atlas",
    "size": "M",
    "material": "Atlas", #remove duplicates
    "material": "Cotton", #rewrite value
    "sdf": "M" #create new key word, u can repeate the value
}
print(my_dct)
print(my_dct["material"])
# print(my_dct["M"]) 
# error: "M" is not key
print(len(my_dct)) #return only unique # of pairs(key and value)


#contain str, int, boolean, lists
dct1 = {
    "type": "Manga",
    "name": "Kasane",
    "coloured": False,
    "year": 2013,
    "in stock": [1, 4, 5, 11, 12]
}
print(dct1)
print(type(dct1))


#create dictionaries by dict():
myDict = dict(name = "Johan Liebhaert", age = 23, nick_name = "Monster")
print(myDict)
print(type(myDict))