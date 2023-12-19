# DICTIONARY
dic = {
    "name": "hriday",
    "branch": "ECE",
    "batch": "2025"
}
print(dic["batch"])

info = {
    'name': 'Hriday',
    'age': 23,
    'eligible': True}
# This will throw error
# print(info['name2'])
# this wont throw an error
print(info.get('name2'))
print(info.keys())
print(info.values())
# to print all values
for key in info.keys():
    print(info[key])
    print(f'the value corresponding to the key {key} is {info[key]}')

# Another way
print(info.items())
for key, value in info.items():
    print(f'{key} is {value}')

# Dictionaries Method
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)
ep1.pop(122)
ep1.popitem()  # remove last value
