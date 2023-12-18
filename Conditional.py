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

def calmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)
a=9
b=22
calmean(a,b)