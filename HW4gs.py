def summation(a,x,index):
    j = len(a)
    temp = 0
    for i in range(j):
        if i != index:
            temp += a[i] * x[i]
    return temp

def maxerror(xactual,xguess):
    l = len(xactual)
    max = 0
    for i in range(l):
        temp = abs(xactual[i] - xguess[i])
        if temp > max:
            max = temp
    
    return max

maxiterations = 100
epsilon = .01
A = [[10,1,2,3,4],[1,9,-1,2,-3],[2,-1,7,3,-5],[3,2,3,12,-1],[4,-3,-5,-1,15]]
b = [12,-27,14,-17,12]
x = [0,0,0,0,0]
xold = list(x)
needed = 0

for k in range(maxiterations):

    for i in range(len(A[0])):
        x[i] = (b[i] - summation(A[i],x,i))/A[i][i]

    if maxerror(x,xold) < epsilon or k + 1 == maxiterations:
        needed = k + 1
        break

    xold = list(x)

with open("HW4gs.txt","w") as f:
    f.write(f"Gauss-Seidel\n")
    f.write(f"Epsilon = {epsilon}\n")
    f.write(f"Max Change in x: {maxerror(x,xold):.6e}\n")
    f.write(f"Number of iterations: {needed}\n\n")
    f.write("Final solution vector x:\n")
    for i, xi in enumerate(x):
        f.write(f"x[{i+1}] = {xi:.8f}\n")