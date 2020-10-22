# Define a class [inherit object(default)]
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.__score = score  # Hidden variable, can't visit by outside method
		self.__score__ = score

	def print_score(self):
		print('%s: %s' % (self.name, self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.score > 80:
			return 'B'
		else:
			return 'C'
  