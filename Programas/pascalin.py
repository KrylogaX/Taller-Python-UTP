n= int(input("introduzca un numero entero\n"))
triangulin = []

for i in range(n):
    triangulin.append([0]*(n))

for i in range (0,n):
    for j in range (0,n):
        if i==0:
            triangulin[i][j] = 1
        elif j==0:
            triangulin[i][j] = 1
        else:
            triangulin[i][j] = triangulin[i][j-1]+triangulin[i-1][j]
            
for i in range (0,n):
    for j in range (0,n):
        if j == n -1:
            print(triangulin[i][j])
        else:
            print(triangulin[i][j],"   ", end = '')

