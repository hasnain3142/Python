names = eval(input("Enter a list of names: "))
assignments = eval(input("Enter a list of missing assignment counts: "))
grades = eval(input("Enter a list of grades: "))
message = "Hi {}\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"
for name,count,grade in zip(names,assignments,grades):
	print(message.format(name,count,grade,(count*2)+grade))
	
#SOLUTION
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
