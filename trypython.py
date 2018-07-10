# name = input("Enter name: ")
# print ("Hello " + name)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = a + b 
# print(str(a) + " plus " + str(b) + " = " + str(c))

# text = str(input("Please enter a text: "))
# print(text.upper())

# text = str(input("Please enter a text: "))
# print(text.lower())

# text = str(input("Please enter a text: "))
# print(text[::-1])

# number = int(input("Please enter a number: "))
# if number <= 10: 
#     print("Small")
# else: 
#     print("big")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a == b: 
#     print("Same")
# else: 
#     print("Different")

# a = int(input("Enter a number: "))
# if a == 1:
#     name = input("Enter your name: ")
#     print("Your name is " + name)
# elif a == 2: 
#     age  = input("Enter your age: ")
#     print("Your age is " + age)
    
# def addNumbers(): 
#     i = 1
#     total = 0
#     while i <= 10:
#         number = int(input("Enter ten numbers. Enter number " + str(i) + ": "))
#         total += number
#         i += 1
#     print(total)
    
# addNumbers()

# for i in range(0, 11):
#     print(i)

# number = 0
# for i in range(1, 11):
#     x = int(input("please enter a number: "))
#     number += x 
# print(number)

# a = int(input("First number: "))
# b = int(input("Second number: "))
# def addNumber(a, b): 
#     c = a + b
#     return c
# print(addNumber(a, b))

# def evenCheck(n): 
#     if n % 2 == 0: 
#         return True
#     else: 
#         return False 
# print(evenCheck(3))
# print(evenCheck(6))

# def message(): 
#     print("This is the message")
# print(message())
# print(message)

# numberList = [1, 2, 3, 4, 5, 6]
# total=0
# for i in numberList:
#     total += i 
# print(total)

# listOfNumbers = []
# for i in range(0, 100): 
#     listOfNumbers.append(i)
# print(listOfNumbers)

# evenNumbers = []
# for i in range(10, 51, 2):
#     evenNumbers.append(i)
# print(evenNumbers)
# print(len(evenNumbers))

# newList = [[0], [0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]
# print(newList[2])

# evens = []
# for i in range(0, 11):
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# tenList = []
# for i in range(0, 20): 
#     tenList.append(i)
# x = slice(len(tenList)-1, len(tenList))
# y = slice(2, len(tenList))
# q = slice(1, len(tenList)-1)
# print (tenList[x])
# print(tenList[y])
# print(tenList[q])

# def upperCase():
#     text = input("Enter text: ").lower()
#     x = slice(1, len(text))
#     print(text[0].upper() + text[x])
# upperCase()

# student = {
#     "name": "Stein",
#     "age": 30, 
#     "nationality": "Dutch"
# }
# print(student)

# students = {
#     "Peter": {"name": "Peter", "age": 26, "Nationality": "Irish"},
#     "Tom": {"name": "Tom", "age": 26, "Nationality": "Irish"},
#     "Cindy": {"name": "Cindy", "age": 26, "Nationality": "Irish"},
#     "Mark": {"name": "Mark", "age": 26, "Nationality": "Irish"},
#     }
# print(students)
# print(students["Peter"]["name"])

# wordsList = {
#     "Test": len("Test"), 
#     "Another test": len("Another test")
#     }
# print(wordsList)

# musicians = {
#     "peter": {"name": "Peter", "nationality": "Irish", "Gender": "male", "bands": ["band1", "band2", "band3"], "instruments": {"guitar": 90, "drums": 55}},
#     "Saskia": {"name": "Saskia", "nationality": "Dutch", "Gender": "female", "bands": ["band1", "band2", "band3"], "instruments": {"guitar": 70, "drums": 100}},
#     "Max": {"name": "Max", "nationality": "Irish", "Gender": "male", "bands": ["band1", "band2", "band3"], "instruments": {"guitar": 90, "drums": 55}},
#     "Eric": {"name": "Eric", "nationality": "Irish", "Gender": "male", "bands": ["band1", "band2", "band3"], "instruments": {"guitar": 90, "drums": 55}}
# }
# print(musicians["Saskia"])
# print(musicians["Saskia"]["bands"])
# print(musicians["Saskia"]["instruments"]["guitar"])

sample_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
words = sample_string.split()
indent = "    "
a = slice(0, 4)
b = slice(4, 10)
c = slice(10, 16)
d = slice(16, 22)
e = slice(22, 26)
f = slice(26, len(words))
# print(" ".join(words[a]) + "\n" + indent + " ".join(words[b]) + "\n" + indent + indent + " ".join(words[c]) + "\n" + indent + indent + " ".join(words[d]) + "\n" + " ".join(words[e]) + "\n" + indent + " ".join(words[f]))

def area_of_circle(r):
    return 3.141592653 * r ** 2
def volume_sphere(r): 
    return 4/3*3.141592653*r**3
def hypotenusa(a, b):
    import math
    return math.sqrt(a ** 2 + b ** 2)
# print(volume_sphere(6))
# print(area_of_circle(1.1))
# print(hypotenusa(5, 12))

# numbers = [12, 432, 34, 343, 43, 555]
# # print(max(numbers))
# def largestNumber(numbers):
#     for i in numbers: 
#         count = 0
#         for x in numbers:
#             if i < x: 
#                 count += 1
#         if count == 0:
#             return i
# print(largestNumber(numbers))

def removeDuplicates(list): 
    for i in list: 
        for x in list: 
            if x == i: 
                del list[i]