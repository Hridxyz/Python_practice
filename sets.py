s = {2,4,2,6}
print(s)
#it does not take repeated values. they are UNORDERED
#sets are not changeable
print(type(s))
empty = {}
print(type(empty))

#Empty set is dictionary

#to save an empty set
empty = set()
print(type(empty))

#operations in set

s1 = {1,2,7,4,6,9}
s2 = {4,5,0,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
s3 = s1.union(s2)
print(s3)
s1.update(s2) #adds s2 values in s1
print(s1)

print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
# del cities
s1.clear()
print(s1)
var = s2.pop()
print(s2)

