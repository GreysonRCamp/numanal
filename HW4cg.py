def product(x,y):
    n = len(x)

    ret = 0
    for i in range(n):
        ret += x[i] * y[i]

    return ret

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

maxiterations = 100
epsilon = .01
A = [[10,1,2,3,4],[1,9,-1,2,-3],[2,-1,7,3,-5],[3,2,3,12,-1],[4,-3,-5,-1,15]]
n = len(A)
b = [12,-27,14,-17,12]
x = [0,0,0,0,0]
r = vectminus(b,matrixmult(A,x))
v = list(r)
c = product(r,r)
needed = 0

for k in range(n):
    if product(v,v)**(1/2) < epsilon:
        break

    z = matrixmult(A,v)
    t = c / product(v,z)

    x = [x[i] + t * v[i] for i in range(n)]
    r = [r[i] - t * z[i] for i in range(n)]
    
    needed+=1
    d = product(r,r)
    if d**.5 < epsilon*(product(b,b)**.5):
        c = d
        break

    v = [r[i] + (d/c)*v[i] for i in range(n)]
    c = d

with open("HW4cg.txt","w") as f:
    f.write(f"Conjugate Gradient\n")
    f.write(f"Epsilon = {epsilon}\n")
    f.write(f"Residual norm after convergence: {c**.5:.6e}\n")
    f.write(f"Number of iterations: {needed}\n\n")
    f.write("Final solution vector x:\n")
    for i, xi in enumerate(x):
        f.write(f"x[{i+1}] = {xi:.8f}\n")