from separate_func import get_output
from datetime import datetime


# A function that returns nothing
def return_none():
    pass

get_output(
    "# A function that returns nothing\n",
    "This function returns nothing: ",
    return_none())


# Number multiplication
def mul_num(x):
    return x * 2

get_output(
    "# Number multiplication\n",
    "Result of multiplication: ",
    mul_num(35))


# Even number or not?
def is_even(x):
    if x % 2 == 0:
        return "{} is Even".format(x)
    else:
        return "{} is not even".format(x)

get_output(
    "# Even number or not?\n",
    "This number ",
    is_even(222))
get_output("This number ", is_even(223))
get_output("This number ", is_even(224))
get_output("This number ", is_even(225))


# Greater than 10 task
def is_greater(*args):
    l = list(args)
    if l[0] > 10:
        return "Yes, this number - {} - greater than 10".format(l[0])
    else:
        return "No, this number - {} - not greater than 10".format(l[0])

get_output(is_greater(17, 25))
get_output(is_greater(5, 25))
get_output(is_greater(16, 25))


# Lambda function with modulo division
l = lambda x, y: x % y

get_output("# Lambda function with modulo division\n",
			"Result of modulo division: ",
			l(12, 7))
get_output("Result of modulo division: ", l(78, 33))
get_output("Result of modulo division: ", l(-78, 33))
get_output("Result of modulo division: ", l(9, 90))

# Work with decorators

def decorate_lst(func):
	def wrapper(*args, **kwargs):
		start = datetime.now()
		result = func(*args, **kwargs)
		time = datetime.now() - start
		'''
		 In this case, because decorate_lst works first in 80 string,
		 i output time varible, not result.
		 Chain of functions - decorate_list -> gen_lst -> gen output
		'''
		return time
	return wrapper

@decorate_lst
def gen_lst(n):
	lst = []
	for i in range(n):
		if i % 2 == 0:
			lst.append(i * 2)
	return len(lst)

@decorate_lst
def gen_fast_lst(n):
	lst = [i * 3 for i in range(n) if i % 2 != 0]
	return len(lst)

get_output("# Work with decorators\n",
			"Slow list generation by {} seconds\n".format(gen_lst(10 ** 5)),
			"and faster list deneration {}".format(gen_fast_lst(10 ** 5)))

# Use map and filter functions

lst1 = [i for i in range(1, 10, 2)]
# Squared elements of list
sq = list(map(lambda x: x * 2, lst1))

# Even elements of list
ev = list(filter(lambda x: True if x % 3 == 0 else False, lst1))

get_output("# Use map and filter functions\n",
			"Result of map function: {}\n".format(sq),
			"Result of filter function: {}".format(ev))

# Impure function
new_lst = []

def impure(*args):
	for i in args:
		new_lst.append(i)
	global new_lst_len
	new_lst_len = len(new_lst)
	return new_lst[-1]

get_output("# Impure function\n",
			 impure("Marvin", "the", "Paranoid", "Android", "This is impure function: "),
			 "\n",
			 new_lst,
			 "\n",
			 "List length: {}".format(new_lst_len))

# Pure function
def pure(lst, *args):
	return lst + list(args)

some_list = []
new_list = pure(some_list, "Marvin", "the")


get_output("# Pure function\n",
			new_list,
			"\n",
			"Pure function not changed global varible: {}".format(some_list))

# Find min and max numbers in list
def find_min_max(lst):
	min_elem = lst[0]
	max_elem = lst[0]
	for i in lst:
		if min_elem > i:
			min_elem = i
		if max_elem < i:
			max_elem = i
	return "Function returns min {} and max {} list elements".format(min_elem, max_elem)

get_output(find_min_max([5, 75, 13, 325, -7, 64, -324, 17, 999, 1247, -9999]))

# Intercalary year
def is_intercalary_year(year):
	if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
		return "{} - this is not intercalary year".format(False)
	else:
		return "{} - this is intercalary year".format(True)

get_output("# Intercalary year\n",
			is_intercalary_year(2019))

# Get season actions
def season(month_num):
	winter = [1, 2, 12]
	spring = [3, 4, 5]
	summer = [6, 7, 8]
	autumn = [9, 10, 11]

	if month_num in winter:
		return "Winter is coming - watch out for white walkers"
	elif month_num in spring:
		return "Spring rains - take umbrella"
	elif month_num in summer:
		return "Summer is hot - take cold limonade"
	elif month_num in autumn:
		return "Autumn gives paints take photo camera"
	else:
		return "{} - incorrect input data".format(month_num)

get_output("# Get season actions{}".format("\n"),
			season(12),
			"\n" * 2,
			season(3),
			"\n" * 2,
			season(7),
			"\n" * 2,
			season(11),
			"\n" * 2,
			season(24))

# Date verifying
def date(day, month, year):
	year_num_len = len(str(year))

	if is_intercalary_year(year):
		feb = 28
	else:
		feb = 29

	month_days = (31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

	if (day not in range(1, 32)) or (month not in range(1, 13)) or (year_num_len not in range(1, 5)):
		return "Incorrect input"
	elif (day > month_days[month - 1]):
		return "Incorrect input"
	else:
		return "Correct input"

get_output("# Date verifying\n",
			date(30,6,2018))
get_output("# Date verifying\n",
			date(31,6,2018))

# Sorted list
unsorted_list = [1, 25.6, 17, "Marvin", [], "Android", 778, 36,
				 98.5, -17, False, {1: "1"},"Paranoid", True, (1,),
				 25, 368, 49, -18.5, 256, ["Hello", "World"], "!"]


# Numbers selection from list with different types of literal
def num_selection(arr):
	num_arr = []
	for i in arr:
		if type(i) is int or type(i) is float:
			num_arr = num_arr + [i]
	return num_arr


# Getting index of minimal element of list
def get_min_ndx(arr):
	min_elem = arr[0]
	ndx_min_elem = 0
	len_arr = len(arr)

	for i in range(1, len_arr):
		if min_elem > arr[i]:
			min_elem = arr[i]
			ndx_min_elem = i

	return ndx_min_elem


# Sort by selection of the unsorted list
def selection_sort(arr):
	sorted_lst = []
	len_arr = len(arr)
	for i in range(len_arr):
		smallest_ndx = get_min_ndx(arr)
		sorted_lst.append(arr.pop(smallest_ndx))
	return sorted_lst

get_output("# Sorted list\n",
			selection_sort(num_selection(unsorted_list)))