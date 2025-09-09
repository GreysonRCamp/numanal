#https://github.com/GreysonRCamp/numanal/blob/main/hw1p5.py

A1 = [[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]] #The two matrices for the homework
A2 = [[1,1/2,1/3,1/4],[1/2,1/3,1/4,1/5],[1/3,1/4,1/5,1/6],[1/4,1/5,1/6,1/7]]

L1 = [[],[],[],[]] #Makes empty matrices for L1, L2 (A1 = L1L1^T)
L2 = [[],[],[],[]]

for j in range(len(A1[0])): #Cholesky algorithm
    for i in range(len(A1)):
        if i == j: #If the row equals the column, use ljj = sqrt(ajj - sum k=0..j-1(ljk^2))
            temp = 0
            for k in range(j):
                temp += L1[i][k]**2
            L1[i].append(pow(A1[i][j] - temp,1/2))
        
        elif i > j: #If the row is lower than the diagonal, use lij = (aij - sum k=0..j-1(likljk)) / ljj
            temp = 0
            for k in range(j):
                temp += L1[j][k]*L1[i][k]
            temp = A1[i][j] - temp
            L1[i].append(temp/L1[j][j])

for i in range(len(L1)): #Adds zeroes to the area above the diagonal on L1
    while len(L1[i]) != 4:
        L1[i].append(0.0)

#Outputs the matrix A
print("A1 = ")
for i in A1:
    print(" ".join(f"{val:8.5f}" for val in i))

#Outputs L1
print("\n\t\t=\n")
for i in L1:
    print(" ".join(f"{val:8.5f}" for val in i))
print("\n\t\tx\n")

#Makes the transpose of L1 and outputs it
LT1 = [[L1[j][i] for j in range(len(L1))] for i in range(len(L1))]
for i in LT1:
    print(" ".join(f"{val:8.5f}" for val in i))

#Repeats the process for the other matrix
for j in range(len(A2[0])):
    for i in range(len(A2)):
        if i == j:
            temp = 0
            for k in range(j):
                temp += L2[i][k]**2
            L2[i].append(pow(A2[i][j] - temp,1/2))
        
        elif i > j:
            temp = 0
            for k in range(j):
                temp += L2[j][k]*L2[i][k]
            temp = A2[i][j] - temp
            L2[i].append(temp/L2[j][j])

for i in range(len(L2)):
    while len(L2[i]) != 4:
        L2[i].append(0.0)

print("\n\nA2 = ")
for i in A2:
    print(" ".join(f"{val:8.5f}" for val in i))

print("\n\t\t=\n")
for i in L2:
    print(" ".join(f"{val:8.5f}" for val in i))
print("\n\t\tx\n")

LT2 = [[L2[j][i] for j in range(len(L2))] for i in range(len(L2))]
for i in LT2:
    print(" ".join(f"{val:8.5f}" for val in i))