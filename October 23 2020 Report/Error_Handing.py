try:
	fh = open("testfile2", "r")
except IOError:
	print("Error: File is NOT FOUND!!!")
else:
	print("Successfully Reading!")
	fh.close()