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


A = [[3,1,0],[1,3,1],[0,1,3]]
b = [4,5,4]

xactual = [1,1,1]

xold = [0,0,0]
xnew = [0,0,0]

x = []
errors = [1]

for k in range(10):

    for i in range(len(A[0])):
        xnew[i] = (b[i] - summation(A[i],xold,i))/A[i][i]

    xold = list(xnew)

    x.append(list(xnew))

    errors.append(maxerror(xactual,xnew))

headers = ["k", "x1", "x2", "x3", "max e", "max e / last max e"]
rows = []
for k in range(10):
    rows.append([k+1,round(x[k][0], 12),round(x[k][1], 12),round(x[k][2], 12),round(errors[k+1], 12),round(errors[k+1]/errors[k], 12)])

# Function to print/write aligned table
def print_table_to_file(headers, rows, filename):
    all_rows = [headers] + rows
    col_widths = [max(len(str(item)) for item in col) for col in zip(*all_rows)]

    with open(filename, "w") as f:
        # Header
        f.write("  ".join(f"{str(item):<{w}}" for item, w in zip(headers, col_widths)) + "\n")
        f.write("-" * (sum(col_widths) + 2 * (len(col_widths)-1)) + "\n")
        # Data
        for row in rows:
            f.write("  ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths)) + "\n")

# Write table to file
print_table_to_file(headers, rows, "hw3q2jac.txt")