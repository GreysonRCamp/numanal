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
            temp += A[i][j] * x[j]
        Ax.append(temp)
    
    maxr = 0
    for i in range(lx):
        temp = abs(b[i] - Ax[i])
        if temp > maxr:
            maxr = temp
    
    return maxr

def flatten(blockA):
    numblocks = len(blockA)
    blocksize = len(blockA[0][0])
    flatA = []
    for block_row in range(numblocks):
        for i in range(blocksize):
            row = []
            for block_col in range(numblocks):
                row += blockA[block_row][block_col][i]
            flatA.append(row)
    
    return flatA

B = [[4,-1,0],[-1,4,-1],[0,-1,4]]
negI = [[-1,0,0],[0,-1,0],[0,0,-1]]
zerom = [[0,0,0],[0,0,0],[0,0,0]]
b = [0,0,1,0,0,1,0,0,1]

A = [[B,negI,zerom],[negI,B,negI],[zerom,negI,B]]
A = flatten(A)

xold = [0,0,0,0,0,0,0,0,0]

xnew = [0,0,0,0,0,0,0,0,0]

oldres = 1000000
newres = residual(b,A,xold)

with open("hw7q4.txt","w") as f:
    f.write("https://github.com/GreysonRCamp/numanal/blob/main/hw3q4.py\n\n")
    f.write(f"{'Method':<10}{'k':<8}{'Residual':<16}{'Successive Ratio':<18}\n")
    f.write("-"*50 + "\n")

    method = "Jacobi"
    for k in range(100):

        for i in range(len(A[0])):
            xnew[i] = (b[i] - summation(A[i],xold,i))/A[i][i]

        xold = list(xnew)
        oldres = newres
        newres = residual(b, A, xold)
        #print(res)
        if newres < 10**(-2) or k == 99:
            f.write(f"{method:<10}{k+1:<8}{newres:<16.9f}{newres/oldres:<18.6f}\n")
            break

    for x in xold:
        print(round(x,5),end=" ")
    print()

    gsx = [0,0,0,0,0,0,0,0,0]
    gsoldres = 10000
    gsnewres = residual(b,A,gsx)
    method = "GS"

    for k in range(100):
        for i in range(len(gsx)):
            gsx[i] = (b[i] - summation(A[i],gsx,i))/A[i][i]

        gsoldres = gsnewres
        gsnewres = residual(b,A,gsx)

        if gsnewres < 10**(-2) or k == 99:
            f.write(f"{method:<10}{k+1:<8}{gsnewres:<16.9f}{gsnewres/gsoldres:<18.6f}\n")
            break

    for i in gsx:
        print(round(i,5),end=" ")
    print()