def fun(x):
    return 2*x**3 - 1024

a = -2
b = 100

epsilon = .0001

t = (b + a)/2

k = 0

while abs(fun(t)) >= epsilon:
    if fun(a)*fun(t) < 0:
        b = t
    elif fun(b)*fun(t) < 0:
        a = t

    t = (b+a)/2
    k += 1
    # if k >= 1000:
    #     break

print("r =",round(t,4),"\nk =",k)