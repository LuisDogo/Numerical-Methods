import math

def f(x):
    fx = pow(x, 3) - x -2
    return fx


def bisection(a, b, n_max):
    c = (a + b) / 2
    print("c: " + str(c) )
    if(n_max==0):
        return c
    else:
        if(f(a) * f(c) < 0):
            return bisection(a , c, n_max-1)
        else:
            return bisection(c , b, n_max-1)


n_max = int(input("N máximo de iteraciones: "))

a = int(input("a: "))
b = int(input("b: "))

if(f(a) * f(b) <= 0):
    print("function root is aprox. in  " + str(bisection(a, b, n_max)))
else:
    print("The interval given to the function wont contain any roots")
    a = int(input("a: "))
    b = int(input("b: "))