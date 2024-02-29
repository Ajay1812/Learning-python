# print("Mummy")
# print("ajay")

name = "Ajay"
age = 23 

# print(f"My name is {name}")
# print(f"My age is {age}")
 
# print(type(name))
# print(type(age))

name1 = "Ajay"
name2 = "Rohit"
name3 = """Yo Yo Honey Singh"""

# print(name1,name2, name3)

age2 = 27
old = False
new = None

# print(type(age2))
# print(type(old))
# print(type(new))

# a = 10
# b = 5 
# sum = a+b
# print(sum)

# light = input("Traffic Light: ").lower()

# if (light == "red"):
#     print("STOP")
# elif (light == "yellow"):
#     print("Look")
# elif (light == "green"):
#     print("GO")
# else:
#     print("Light Broken")

# food = input("Food : ")
# eat = "Yes" if food == "Cake" else "No"
# print(eat)

# print("Sweet") if food == "Cake" or food == "kesar barfi" else print("Not Sweet")


# age = int (input ("age : "))
# vote = ("No", "Yes") [age >= 18] # (False value, True value)
# print(vote)

# movie1 = input("Enter a movie name: ")
# movie2 = input("Enter a movie name: ")
# movie3 = input("Enter a movie name: ")

# lst = []
# lst.append(movie1)
# lst.append(movie2)
# lst.append(movie3)

# print(lst)


# lst = [1, 2, 3, 2, 1]
# lst1 = lst.copy()
# lst1.reverse()

# if (lst == lst1):
#     print("palin")
# else:
#     print("not palin")


# marks = ("C", "D", "A", "A", "B", "B", "A")
# print(marks.count("A"))

# dict = {
#     "cat":"a small animal",
#     "table": ["a piece of furniture", "list of facts and figure"]
# }
# print(dict)


# subjects = {"python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"}

# print(len(subjects))

# math = int(input("Maths Marks: "))
# phy = int(input("Physics Marks: "))
# chem = int(input("Chemistry Marks: "))

# dict = {}

# dict.update({"math":math})
# dict.update({"phy":phy})
# dict.update({"chem":chem})

# print(dict)

# store = {
#     ("float",9.0),
#     ("int",9)
# }
# print(store)


# count = 1
# while count <= 100:
#     print(count)
#     count+=1


# count = 100
# while count >= 1 :
#     print(count)
#     count-=1

# n = int(input("Enter a number: "))

# i = 1
# while i <= 10:
#     print(f"{i} X {n} = {i * n}")
#     i+=1


# lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in lst:
#     print(i)

# search = int(input("Find x : "))

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# for i in tup:
#     if (i == search):
#         print("Found the element","At index: ",tup.index(search), "search: ", i)
#         break
#     else:
#         print("Not Found")
#         break

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in num:
#     print(val)


# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for i in tup:
#     if (i == x):
#         print("number found at: ", idx)
#         break
#     idx+=1

# n = int(input("Enter n: "))

# i = 1
# sum = 0
# while i<=n:
#     sum += i
#     i+=1

# print("Sum: ",sum)

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i

# print("Factorial: ",fact)

cities = ['delhi','mathura','gurgoan','mumbai',"noida","pune"]

def lenOfCities(cities):
    return len(cities)

# print(lenOfCities(cities))

def singleLineOutput(list):
    for i in list:
        print(i, end=" ")

# singleLineOutput(cities)

def findFact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact


# print(findFact(5))

def converter(usd):
    inr = usd * 83
    return inr


# print(converter(10))

def oddEven(n):
    if n % 2==0: 
        return "Even"
    else:
        return "Odd"

# print(oddEven(12123123123))
    
# recursive function
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

# show(5)
    

def cal_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * cal_fact(n-1)
    
# print(cal_fact(5))
    
def sum(n):
    if n == 0:
        return 0
    else:
        val = 0
        val = sum(n-1) + n
        return val
    
# print(sum(10))


heros = ["batman","superman","spiderman","shaktiman","thor"]

def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

# print_list(heros)
    

# File I/O
# f = open('demo.txt', 'r')
# data = f.read()
# data = f.readline()
# print(data, type(data))
# f.close()

# f = open('demo.txt', 'r+')  
# f = open('demo.txt', 'w')
# f = open('demo.txt', 'a')
# data = f.write("\nYo Yo  ")
# f.close()

# with open ("demo.txt", "r") as f:
#     data = f.read()
#     print (data)

# import os

# os.remove('demo.txt')
    
 

# with open('sample.txt', 'r') as f:
#     data = f.read()
# newData = data.replace("Java", "Python")
# print(newData)


# with open('sample.txt', 'w') as f:
#     f.write(newData)

def check_for_word(word):
    with open('sample.txt', 'r') as f:
        data = f.read()
        if data.find(word) != -1 :
            print("Found")
        else:
            print("Not Found")

def check_for_line(word):
    data = True
    line = 1
    with open('sample.txt', 'r') as f:
        while data:
            data = f.readline() 
            if (word in data):
                return line
            line+=1
    return -1

# print(check_for_line("Ajay"))

count = 0
with open('demo.txt', 'r') as f:
    data = f.read()
    num = data.split(',')
    for i in num:
        if (int(i) % 2 == 0):
            count+=1
print(count) 