# While loops
x = 1
while x < 5:
	print(x)
	x = x + 1  # Consider: x += 1

# simple iterations using: range()
for i in range(10):
	print(i)

# Loop Over String
for c in "python":
	print(c.capitalize())

# Loop Over List
areas = [1, 2, 3, 4]
for item in areas:
	print(item)
# With enumerate
for index, value in enumerate(areas):
	print(index+1, value)

# Loop Over Dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo',
		  'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}
# Iterate over europe
for key, value in europe.items():
	print("The capital of " + key + " is " + value)
	print(europe.keys())
for key in europe.keys():
	print("The capital of " + key + " is " + europe[key])

# Loop Over Numpy Array
import numpy as np
# Loop over 1-d array
np_array = np.array([1, 2, 3, 4])
for x in np_array:
	print(x)
	
dl = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
np_array2d = np.array(dl)
print(np_array2d)

# Loop over 2-d array, Go through each element in 2d array
for item in np.nditer(np_array2d):
	print(item)
for item in np_array2d:
	print(item)


