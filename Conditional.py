# a = int(input("Enter your age\n"))
# print("Your age is :", a)
#
# if(a>18):
#     print("You can drive")
# else:
#     print("you cannot drive")
# if else elif
# read time
# import time
#
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = int(time.strftime('%H'))
# if timestamp < 12:
#     print('Good Morning')
# elif 12 < timestamp < 17:
#     print('Good Afternoon')
# else:
#     print('Good Evening')
# # for loops
# name = "hriday"
# for i in name:
#     print(i, end=",")
#     if i == "d":
#         print("\nD hain isme")
# colors = ["Red", "Green", "blue"]
# for color in colors:
#     print (color)
#     for i in color:
#         print(i)
# for k in range(5):
#     print(k+1)
# for k in range(1,9):
#     print(k)
# range(n,m) it goes from n to m-1
# for k in range(1,210,3): #start stop step
#     print(k)
# while loop
i = 0


# while (i < 3):
#     print(i)
#     i = i + 1
# else:
#     print("out")
# # do while
# for k in range(10):
#
#     if k == 4:
#         break
#     print(k)

#
# tuples
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum / len(numbers))
#
#
# average(5, 6, 11, 13, 82)


# defining dictionary
# def name(**name):
#     print("hello", name["fname"], name["mname"])
#
#
# name(mname="Hriday", lname="Paras", kname="Bhagtani")
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     return sum / len(numbers)
#
#
# c = average(5, 6, 11, 13, 82)
# # print(c)
# marks = [3,4,5,"hriday", True]
# type(marks[4])
# print(marks)
# print(marks[3])

#LIST COMPREHENSION

# lst = [i for i in range(4)]
# print(lst)
# lst2 = [i*i for i in range(4)]
# print(lst2)
# lst3 = [i*i for i in range(100) if i%2==0]
# print(lst3)
#
# l=[1,2,22,56,34,3,4,5]
# print(l)
# l.append(9)
# # l.sort(reverse=True)
# l.reverse()
# print(l.index(4))
# print(l.count(5))
# print(l)
# m= l.copy()
# m.insert(4,2345)
# print(m)
# k = [389433,34,546]
# l.extend(m)
# print (l)
# k=l+m
# print(k)

#TUPLES
#you cant change tuple
tup2 = (1,2,3,4,7,4,5)
print(tup2)
print(type(tup2))

#COVERTING TUPLES TO LIST AND VICE VERSA
countries = ("India","Spain","Italy","England")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
countries = tuple(temp)
print (countries)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1. index(3, 4, 8)
print( 'Count of 3 in tuplel is:', res)
