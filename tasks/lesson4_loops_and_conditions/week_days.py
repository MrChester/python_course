days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_numbers = [1, 2, 3, 4, 5, 6, 7]

day_dict = dict(zip(days, day_numbers))

for k, v in day_dict.items():
	if v < 6:
		print(v, k, ' - Just another working day')
	else:
		print(v, k," - Yoo-Hoo! Day offs beginning! Let's get party")
