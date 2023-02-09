# task 1:
n = float(input())
def gram_to_ounc(n):
    print(n*28.3495231)

gram_to_ounc(n)



#task 2:
F = float(input())
def calculated(F):
    C = (5/9)*(F-32)
    print("C = ", C)

calculated(F)


#task 3:
def solve(numheads, numlegs):
    rabbits = ((numlegs - numheads) - numheads)/2
    chickens = 35 - rabbits
    print("Chikken = ", chickens)
    print("Rabbits = ", rabbits)
solve(35, 94)


#task 4:
numbers = list(map(int, input().split()))

def filter_prime(numbers):
    if numbers == 1 or numbers == 0:
        return False
    for i in range(2, int(numbers**0.5 + 1)):
        if numbers % i == 0:
            return False
    return True
        

for i in range(len(numbers)):
    if(filter_prime(numbers[i])):
        print(numbers[i], end=' ')


#task 5:
#permutation
import itertools

def perms(str):
    if len(str) == 0:
        return ['']
        #generation of remaining perms in str
        remain = perms(str[1:len(str)])
        
        #generation by inserting 1st char
        permone = []
        for i in range(0, len(remain)):
            for j in range(0, len(str)):
                #new str <- first char
                nstr = remain[i][0: j] + str[0] + remain[i][j: len(str) - 1]
                if nstr not in permone:
                    permone.append(nstr)
                    return permone #returning results

inp = input()
print(perms(inp))


#task 6:
s = input().split()
def reverse(s):
    print(*str[::-1]) 

reverse(s)


#task 7:
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
            else: pass
        else: pass
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


#task 8:
def spy_game(nums):
    s = ''  #empty storage
    for i in range(len(nums)): #iterating btw the range
        if nums[i] == 0 or nums[i] == 7:
            s+=str(nums[i]) #adding 007 to storage
    if '007' in s: #checking if 007 is contained here
        return True
    else:
        return False
            

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#task 9:
r = float(input())
def sphere(r):
    print(((4*3.14*(r**3)))/3)

sphere(r)


#task 10:
a = list(map(int, input().split())) #array input
u = [] #empty list

def unique(a, u):
    if a not in u:
        u.append(a)  #adding and checking if theres repeated values
    
for i in range(len(a)):
    unique(a[i], u)    #using unique func
    
print(u)


#task 11:
str = input()

def palindrome(str):
    if str[::-1] == str[::1]:
        return True
    return False

print(palindrome(str))


#task 12:
a = list(map(int, input().split()))

def histo(a):
    for i in a:
        for x in range(i):    #to iterate inside the array to put stars
            print('*', end='')
        print('')
        
histo(a)


#task 13:
from random import random, randint, randrange

def guess(name):
    num = randint(1, 20)
    att = 1
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    while True:
        print('Take a guess.')
        inp = int(input())
        if inp == num:
            print(f'Good job, {name}! You guessed my number in {att} guesses!')
            break
        else:
            print('Your guess is too low.')
            att+=1
    
    
print('Hello! What is your name?')
name = input()
guess(name)
