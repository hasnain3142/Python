def my_range(x):
	i = 0
	while i<x:
		yield i
		i += 1
for y in my_range(8):
	print(y)
	
