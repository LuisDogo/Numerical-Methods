import Convergence

def f(x):
    fx = pow(x, 4) - pow(x, 2) * 2 + 3 * x - 5
    return fx

def xe(a, b, n_max):
    if n_max > 0:
        num = (a * f(b)) - (b * f(a))
        den = f(b) - f(a)
        c = num / den
        n_max -= 1
        print("c: " + str(c) + "    f(c): " + str(f(c)))
        if c == 0:
            print("Root ≈ " + str(c))
        else:
            if f(a) * f(c) < 0:
                return xe(a, c, n_max)
            else:
                return xe(c, b, n_max)
        

n_max = int(input("n_max: "))
a = int(input("a: "))
b = int(input("b: "))
xe(a, b, n_max)