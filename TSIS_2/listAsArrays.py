#Work with lists as arrays:
cars = ["Ford", "Volvo", "BMW", "Ford", "Volvo"]
print(cars)
print(cars[2]) #return car in index 2

cars[2] = "Toyota" #change value
print(cars)

print(len(cars))

#for loop & array:
for i in cars:
    print(i)

#add element:
cars.append("Honda")
print(cars)

#delete element:
cars.pop(0)
print(cars)

#remove elements:
cars.remove("Volvo") #remove only first apperence
print(cars)