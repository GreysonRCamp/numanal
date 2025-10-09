def summation(a,x,index):
    j = len(a)
    temp = 0
    for i in range(j):
        if i != index:
            temp += a[i] * x[i]
    return temp

def residual(b,A,x):
    Ax = []
    lx = len(x)
    lA = len(A[0])
    for i in range(lx):
        temp = 0
        for j in range(lA):
            temp += A[i][j] * x[i]
        Ax.append(temp)
    #print(Ax)
    maxr = 0
    for i in range(lx):
        temp = b[i] - Ax[i]
        if temp > maxr:
            maxr = temp
    
    return maxr

B = [[4,-1,0],[-1,4,-1],[0,-1,4]]
negI = [[-1,0,0],[0,-1,0],[0,0,-1]]
zerom = [[0,0,0],[0,0,0],[0,0,0]]
b = [0,0,1,0,0,1,0,0,1]

A = [[B,negI,zerom],[negI,B,negI],[zerom,negI,B]]

x = [0,0,0,0,0,0,0,0,0]

notblockA = []

for row in A:
    for i in range(len(row)):
        temp = []
        for j in range(len(row[0])):
            for k in range(len(row[0][0])):
                temp.append(row[j][i][k])
        notblockA.append(temp)
    
A = list(notblockA)

oldres = 1000000
newres = 0

for k in range(100):

    for i in range(len(x)):
        x[i] = (b[i] - summation(A[i],x,i))/A[i][i]

    oldres = newres
    newres = residual(b,A,x)
    if newres < 10**(-2):
        print("k =",k+1)
        break
    if k == 99:
        print("k = 100")

for i in x:
    print(round(i,5),end=" ")
print()
print(newres)
print(newres/oldres)