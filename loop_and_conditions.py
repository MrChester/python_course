# three numbers comparison
a = int(input())
b = int(input())
c = int(input())

if (a == b) or (a == c) or (b == c):
	print("YES")
else:
	print("ERROR")


# one number is the sum of the other two
d = int(input())
e = int(input())
f = int(input())

if (d == e + f) or (e == d + f) or (f == d + e):
	print("YES")
else:
	print("ERROR")