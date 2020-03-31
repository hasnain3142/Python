def my_range(x):
	i = 0
	while i<x:
		yield i
		i += 1
for y in my_range(8):
	print(y)
	
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    i = 0
    while i < len(iterable):
        yield start, iterable[i]
        i += 1
        start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
