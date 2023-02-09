#task 1:
class Strings:
    def __init__(self, getString):
        self.getString = getString
    def printString(self):
        return self.getString.upper()
        
s = Strings(input())
print(s.printString())


#task 2:
class Shape:
    def __init__(self, area):
        self.area = 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__(area)
    def area(self):
        return self.length * self.length


#task 3:
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


#task 4:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


#task 5:
#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("+deposit")

    def withdraw(self, money):
        if amount > self.balance:
            print("you're poor")
        else:
            self.balance -= money
            print("you can withdraw")


#task 6:
#Write a program which can filter prime numbers in a list by using filter function. 
#Note: Use lambda to define anonymous functions.

numbers = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)