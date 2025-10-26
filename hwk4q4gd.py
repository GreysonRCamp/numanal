def matrixmult(A,x):
    n = len(x)
    ret = []
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += A[i][j] * x[j]
        ret.append(temp)

    return ret

def vectadd(u,r):
    n = len(u)
    ret = list(u)
    for i in range(n):
        ret[i] += r[i]

    return ret

def vectminus(b,Ax):
    n = len(b)
    ret = list(b)
    for i in range(n):
        ret[i] -= Ax[i]
    
    return ret

def inorm(r):
    return sum(ri*ri for ri in r)

def squaredanorm(r,A):
    n = len(r)
    rA = []
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += r[j] * A[j][i]
        rA.append(temp)

    ret = 0
    for i in range(n):
        ret += rA[i]*r[i]

    return ret

A = []
b = []
x = []
epsilon = .01
n = 16 #Change to 32 if you want to check that

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(1/(1+(i+1)+(j+1)))
    A.append(temp)
    s = sum(temp)/3
    b.append(s)
    x.append(0)

r = vectminus(b,matrixmult(A,x))
check = inorm(r)

k = 0
while check >= epsilon and k < 10000:
    scale = inorm(r)/squaredanorm(r,A)
    x = vectadd(x,[scale * ri for ri in r])
    r = vectminus(b,matrixmult(A,x))
    check = max(abs(ri) for ri in r)
    k += 1

# print(check,"\n")
# for i in x:
#     print(i)
# print("\n",k)

with open("hwk4q4gd.txt","w") as f:
    f.write(f"Gradient Descent\nSize of matrix = {n} x {n}\n")
    f.write(f"Epsilon = {epsilon}\n")
    f.write(f"Residual norm after convergence: {check:.6e}\n")
    f.write(f"Number of iterations: {k}\n\n")
    f.write("Final solution vector x:\n")
    for i, xi in enumerate(x):
        f.write(f"x[{i+1}] = {xi:.8f}\n")