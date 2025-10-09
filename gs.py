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
xguess = [0,0,0]
x = []
errors = [1]

for k in range(10):

    for i in range(len(xguess)):
        xguess[i] = (b[i] - summation(A[i],xguess,i))/A[i][i]

    x.append(list(xguess))
    errors.append(maxerror(xactual,xguess))

print(x[9])

headers = ["k", "x1", "x2", "x3", "max e", "max e / last max e"]
rows = []
for k in range(10):
    rows.append([k+1,round(x[k][0], 12),round(x[k][1], 12),round(x[k][2], 12),round(errors[k+1], 12),round(errors[k+1]/errors[k], 12)])

# Function to print/write aligned table
def print_table_to_file(headers, rows, filename):
    all_rows = [headers] + rows
    col_widths = [max(len(str(item)) for item in col) for col in zip(*all_rows)]

    with open(filename, "w") as f:
        f.write("https://github.com/GreysonRCamp/numanal/blob/main/gs.py\n")
        # Header
        f.write("  ".join(f"{str(item):<{w}}" for item, w in zip(headers, col_widths)) + "\n")
        f.write("-" * (sum(col_widths) + 2 * (len(col_widths)-1)) + "\n")
        # Data
        for row in rows:
            f.write("  ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths)) + "\n")

# Write table to file
print_table_to_file(headers, rows, "hw3q2gs.txt")