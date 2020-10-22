# List of lists, NOTED: Row First! same as C
house = [['living room', 25], ['bed room', 13], ['bathroom', 9.1]]
print(house[0])
print(house[1][1])
print(house[:])

# List Operations
x = ["a", "b", "c", "d"]
print(x)
del(x[1])
print(x)
x = x + ['e']  # what about? x = x + 'e'
print(x)
x.append('e2')
print(x)

# Copy list !!!Should be NOTED!
x = ["a", "b", "c", "d"]
y = x
z = x[:]
print(x, y, z)
x[0] = 'A'
print(x, y, z)

# function, method on list
x = ["a", "b", "c", 2]
print(len(x))
print(type(x[0]), type(x[3]))
y = sorted(x[0:3], reverse=True)
print(y)
x.append('e')
print(x)


# Define a Tuple
T = (123, 45, 'hello')
print(T[0])
# T[0] = 234

# Tuple Packing and Unpacking
T = 1, 'str', True
x, s, b = T
print(s)

# Tuple is immutable, however, could be mutable using a list
T = ('A', 'B', ['A', 'B'])
print(T[0])
print(T[2])
T[2][0] = 'X'
print(T[2])

# element in Set is Unique, Unordered
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('apple' in basket)

# Set Operations: Union, Intersection, Difference, etc
a = set('abracadabra')
b = set('alacazam')
print(a, b)
print('Set Union: ', a|b)
print('Set Intersection: ', a&b)
print('Set Difference: ', a-b)
print('Set Symmetric Difference: ', a^b)  # letters in a or b but not both
print('Set ymmetric Difference: ', (a|b) - (a&b))

# Define a dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway': 'oslo'}
print(europe['france'])
print(europe.keys())

# KEY Should be Unique
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway': 'oslo'}
print(europe['spain'])
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway': 'oslo', 'spain':'****'}
print(europe['spain'])
## Any immutable values can be the KEY
dict = {0:'value1', True:'value2', 12:14}
print(dict[0], dict[True], dict[12])


## Operations on Dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway': 'oslo'}
#### add item in dict
europe['italy'] = 'rome'
print('italy' in europe)
#### update item in dict
europe['spain'] = 'Madrid'
#### remove item in dict
del(europe['spain'])
print(europe)

# Dictionary in Dictionary
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
'france': { 'capital':'paris', 'population':66.03 },
'germany': { 'capital':'berlin', 'population':80.62 },
'norway': { 'capital':'oslo', 'population':5.084 } }
print(europe['france']['capital'])
data = {'capital':'rome', 'population':59.83}
europe['italy'] = data
print(europe)












