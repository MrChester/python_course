# Basic output separator with decorator func
def separate_this(func):
	def wrapper(*param):
		print("===========")
		print()
		func(*param)
		print()
	return wrapper

@separate_this
def get_output(*param):
	print("".join(map(str,param)))