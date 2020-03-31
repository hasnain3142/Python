f = open("some_files.txt","r")
content = f.read()
print(content)
f.close()

with open("new_files.txt","w") as f:
	f.write("Hello, World")
	f.close()
