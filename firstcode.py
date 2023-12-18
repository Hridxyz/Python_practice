print("first code")
print("use of comments and new line \nthis is new line") #use hashtag
'''multiple cline comment
second line'''
print("use of escape sequence \"hey\" use of double collin")
print("hey", 6, 7, sep="~", end="009\n")
#variables
a=1
name="hriday"
print(type(a))
list1 = [8, 2.3, [4,5], ["hriday", "paras"]]
print(type(list1))
dict1 = {"name": "Hriday", "age": 22, "candrive": True}
#operators
print(15//6) #only prints decimal part
print(5**4) #exponential operator
#typecasting
a="2"
b="4"
print(int(a)+int(b)) #typecasted
print(a+b)
#input
# k = input()
# print(k)
# m = input("your name: ")
# print (m)
# #input is taken as string, it has to be typcasted as integer if we are entering integer
# x = input( "Enter first number: ")
# y = input( "Enter second number: ")
# print(x + y)
# print(int(x) + int(y))
#multi line string
line = """line1
line 2
line 3"""
print(line)
print(name[0])
print( " lets use for loop\n")
# for character in line:
#     print(character)
names2= "hriday,paras"
print(names2[0:6])
print(names2[0:-2])
print(names2[-5:-2])
nm = "Harry"
print(nm[-4:-2])
#print everything in upper case
#strings are immutable
print(name.upper())
print(name.lower())
d = "strip string!!!!"
print(d.rstrip("!"))
print(d.replace("strip", "Paras"))
#split
print(d.split(" "))
print(d.capitalize())
print(d.center(25))
print(d.count("s"))
print(d.endswith("!"))
print(d.endswith("!", 7,9))
str1 = """He's
name is Dan. He is an
honest man."""
print(str1. find( "is"))
str2 = "WelcomeToTheConsole"
str3 = "\nWelcomeToTheConsole"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isspace())
print(str2.isprintable())
print(str3.isprintable()) #\n is not printable
print(str1.swapcase())
print(str1.title())
