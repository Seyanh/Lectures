def echo_word(word1, echo):
	"""Concatenate echo copies of word1."""
	words = word1 * echo
	return words
print(echo_word('hey ', 5))

# Using lambda function
echo_word = (lambda word1, echo: word1 * echo)
print(echo_word('hey ', 5))

# lambda function with no arguments
fun = (lambda : print('Hi'))
fun()



nums = [2, 4, 6, 8, 10]
result = map(lambda a: a ** 2, nums) #generator
print(result)
for i in result:
	print(i)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)
# Convert result to a list: result_list
result_list = list(result)
# Print result_list
print(result_list)

## Reduce function for accumulative calculation
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4,5])

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 +" "+ item2, stark)
# Print the result
print(result)


