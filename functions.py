# def printHello():
#     print("hello world!")
#
#
# printHello()
# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
#     return p
#
#
# marks1 = [45, 86, 78, 77]
# percent1 = percent(marks1)
#
# marks2 = [34, 56, 78, 90]
# percent2 = percent(marks2)
#
# # print(percent1, percent2)
# def greet(name):
#     print("good day, " + name)
# greet("bunty")
# def greet(name):
#     gr = "hello " + name
#     return gr
# a = greet("bunty")
# print(a)
# positional argument
# def add(n1, n2):
#     sum = n1 + n2
#     return sum
#
#
# # print("the sum is ", add(3, 4))
# #keyword argument
# def add(n1, n2):
#     sum = n1 + n2
#     return sum
#
# print("the sum is ", add(n1=3, n2=4))
# default argument
# def add(n1, n2=0):
#     sum = n1 + n2
#     return sum
# print("the sum is", add(3))
# default argument2
# def add(n1=0, n2=0):
#     sum = n1 + n2
#     return sum
# print("the sum is ", add())

# arbitary argument **args

# def addallnumber(*args):
#
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# op = addallnumber(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print("the sum is ", op)

# def studentinfo(**kwargs):
#     for x, y in kwargs.items():
#         print(x, "is", y)
#
#
# studentinfo(name="bunty", age=24, city="mumbai")
# studentinfo(name="raj", age=43, city="delhi")


# def sumoneton(n):
#     sum = 0
#     fo
# print("sum of all no till n is", output)r i in range(1, n+1):
#         sum += i
#     return sum
# n = int(input("enter n:"))
# output = sumoneton(n)
# print("sum of all number till n is", output)

# def sumoneton(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum
# n = int(input("enter n:"))
# output = sumoneton(n)

# def outer_function():
#     x = 1
#
#     def inner_function():
#         y = 2
#         result = x + y
#         return  result
#     return inner_function
# output = outer_function()

# def addone(x):
#     x = x+1
#     print("inside function:", x)
# x = 5
# addone(x)
# print("outside function:", x)

# def modifylist(lst):
#     lst.append(4)
#     print("inside function:", lst)
#
# lst = [1, 2, 3]
# modifylist(lst)
# print("outside function:", lst)

# def factorial(n):
#     ans = 1
#     if n == 0:
#         ans = 1
#     else:
#         for i in range(1, n+1):
#             ans *= i
#     return ans
# n = int(input("enter n:"))
# output = factorial(n)
# print("the factorial is:", output)





























































