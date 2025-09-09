#https://github.com/GreysonRCamp/numanal/blob/main/hw1p4.py

xstorage = [] #Stores the solutions u and x values for plotting
ustorage = []

for n in range(1,9): #For values of n = 1 ... 8
    N = pow(2,n) - 1 #Sets N and h based on the current n
    h = pow(2,-n)
    
    eps = pow(10,-3) #Value for the sub and super diagonal, where all values are 10^-3
    a = (2*eps + pow(h,2)) / pow(h,2) #The values for the main diagonal on A
    b = -eps / pow(h,2) #The values for the other diagonals

    f = []
    x = []
    for i in range(1, N + 1): #Sets up vector f and the x values for plotting
        f.append(2*i*h + 1)
        x.append(i*h)


    w = [a] #Holds the diagonal values for U and L
    l = [None] #Has an empty value so the lists w and l are the same size

    for i in range(1, N): #Makes L and U
        l.append(b/w[i-1]) #Makes the main diagonal on L
        if i != N - 1:
            w.append(a-l[i]*b) #Makes the main diagonal on U
        else:
            w.append(a) #Set wn = an

    #Thomas Algorithm
    #Ly = f
    y = [f[0]]

    for i in range(1,N):
        y.append(f[i] - l[i]*y[i-1])

    #Uu = y
    u = [y[N-1]/w[N-1]]

    for i in range(N-2,-1,-1):
        temp = (y[i] - b*u[0])/w[i]
        u.insert(0,temp)

    xstorage.append(x)
    ustorage.append(u)

#The rest of the code plots the results and saves the plots to a pdf for viewing
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages("hw1p4plots.pdf") as pdf:
    for i in range(8):
        plt.scatter(xstorage[i],ustorage[i],color=(0,56/255,49/255), marker='o')
        plt.xlabel("xi")
        plt.ylabel("ui")
        plt.title("n = " + str(i + 1))
        pdf.savefig()
        plt.close()