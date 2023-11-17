# fruits = ["apple", "banana", "cherry", "papaya"]
# print(fruits)
# print(type(fruits))
# print(len(fruits))
# if "banana" in fruits:
#     print("banana is part of the list")
# if "banana" not in fruits:
#     print("banana is not part of the list")
# List = [10, 20, 30, 40]
# var = List[-3:-1]
# print(var)


n = int(input("enter size of a list :"))
list = []

for i in range(n):
    num = int(input())
    list.append(num)
print(list)

idx1 = int(input("enter index1:"))
idx2 = int(input("enter index2:"))


temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)















