def mat_print(m):
    for r in m:
        for e in r:
            print(e,end=" ")
        print()
def mat_input():
    global n
    n = int(input("Enter order of a sqaure matrix: "))
    m = []
    for i in range(1, n + 1):
        r = input(f"Enter elements of row: {i}: ").split()
        m.append([int(e) for e in r])
    return m

m1,m2 = mat_input(),mat_input()
print(m1,m2)
print("Matrix 1")
mat_print(m1)
print("Matrix 2")
mat_print(m2)
print("Select one of the following operations:\n1.Addition\n2.Subraction\n3.Multiplication\n4.Transpose")
ch = input()
if ch=="1":
    m = []
    for i in range(n):
        r=[]
        for j in range(len(m1)):
            sum=m1[i][j]+m2[i][j]
            r.append(sum)
        m.append(r)
    mat_print(m)
elif ch == "2":
    m = []
    for i in range(n):
        r = []
        for j in range(len(m1)):
            sum = m1[i][j] - m2[i][j]
            r.append(sum)
        m.append(r)
    mat_print(m)
elif ch=="3":
    c = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                c[i][j] += m1[i][k]*m2[k][j]
    mat_print(c)
elif ch=="4":
    a = input("Enter matrix number: ")
    m = []
    for i in range(n):
        r = []
        for j in range(len(m1)):
            new = eval("m"+a)[j][i]
            r.append(new)
        m.append(r)
    mat_print(m)
else:
    print("Please enter correct operation number")



