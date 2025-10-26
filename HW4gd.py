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

maxiterations = 100
epsilon = .01
A = [[10,1,2,3,4],[1,9,-1,2,-3],[2,-1,7,3,-5],[3,2,3,12,-1],[4,-3,-5,-1,15]]
b = [12,-27,14,-17,12]
x = [0,0,0,0,0]
r = vectminus(b,matrixmult(A,x))
check = inorm(r)
needed = 0

for k in range(maxiterations):
    if check < epsilon:
        needed = k+1
        break

    scale = inorm(r)/squaredanorm(r,A)
    x = vectadd(x,[scale * ri for ri in r])
    r = vectminus(b,matrixmult(A,x))
    check = max(abs(ri) for ri in r)

    if k + 1 == maxiterations:
        needed = k+1

with open("HW4gd.txt","w") as f:
    f.write(f"Gradient Descent\n")
    f.write(f"Epsilon = {epsilon}\n")
    f.write(f"Residual norm after convergence: {check:.6e}\n")
    f.write(f"Number of iterations: {k}\n\n")
    f.write("Final solution vector x:\n")
    for i, xi in enumerate(x):
        f.write(f"x[{i+1}] = {xi:.8f}\n")