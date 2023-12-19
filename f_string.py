#WITHOUT FSTRING
letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Hriday"
print(letter.format(country, name))
letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "Hriday"
print(letter.format(country, name))

#F STRING
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
#To round off to points only
txt = "For only {price:.2f} dollars"
print(txt.format(price = 49.09999))

#Docstring

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)
print(square.__doc__)
