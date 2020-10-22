# Simple example
def fun_name(var1='default value'):
	var = var1*3
	print(var)
fun_name('test ')
fun_name()

# Nested Functions: NOTE: SCOPE
def three_shouts(word1, word2, word3):
	"""Returns a tuple of strings

    concatenated with '!!!'."""

	# Define inner
	def inner(word):
		"""Returns a string concatenated with '!!!'."""
		return word + '!!!'
	# Return a tuple of strings
	return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))



# Nested functions
def echo(n):
	"""Return the inner_echo function."""
	# Define inner_echo
	def inner_echo(word1):
		"""Concatenate n copies of word1."""
		echo_word = word1 * n
		return echo_word
	# Return inner_echo
	return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

## Keyword:'nonlocal' in inner nested function
## Questions: Why not global?
# Define echo_shout()
def echo_shout(word):
	"""Change the value of a nonlocal variable"""
	# Concatenate word with itself: echo_word

	echo_word = word * 2
	# Print echo_word
	print(echo_word)

	# Define inner function shout()
	def shout():
		"""Alter a variable in the enclosing scope"""
		# Use echo_word in nonlocal scope
		nonlocal echo_word
		# Change echo_word to echo_word concatenated with '!!!'
		echo_word = echo_word + '!!!'

	# Call function shout()
	shout()
	# Print echo_word
	print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')


## Functions with variable-length arguments (*args)
def CatStr(var1, *args): ## CatStr(*args)
	allstr = ""
	for s in args:
		allstr += s
	return allstr
print(CatStr("Hi, ", "How ", "are ", "you "))


## Functions with variable-length Keyword arguments (**kwargs)
# Define report_status
def report_status(**kwargs):
	"""Print out the status of a movie character."""
	print("\nBEGIN: REPORT\n")
	# Iterate over the key-value pairs of kwargs
	for keys, values in kwargs.items():

		# Print out the keys and values, separated by a colon ':'
		print(keys + ": " + values)
	print("\nEND REPORT")
# call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")