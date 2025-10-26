def fun(x): #Really only useful for non-linear equations, linear gives answer right away
    return 2*x**3 - 1024

a = -2
b = 100

epsilon = .0001

t = -((b - a)*fun(a))/(fun(b)-fun(a)) + a

k = 0

while abs(fun(t)) >= epsilon:
    if fun(a)*fun(t) < 0:
        b = t
    elif fun(b)*fun(t) < 0:
        a = t

    k += 1

    t = -((b - a)*fun(a))/(fun(b)-fun(a)) + a

    # if k >= 1000:
    #     break

print("r =",round(t,4),"\nk =",k)