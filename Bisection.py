import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    fx = pow(x, 3) + x - 3
    return fx

def bisection(a, b, n_max, graph_values):
    c = (a + b) / 2
    print("c: " + str(c) )
    graph_values.append(c)
    if(n_max==0):
        return c
    else:
        if(f(a) * f(c) < 0):
            print(str(a) + " " + str(c))
            return bisection(a , c, n_max-1, graph_values)
        else:
            print(str(c) + " " + str(b))
            return bisection(c , b, n_max-1, graph_values)


n_max = int(input("Max number of iterations: "))
graph_values = []
a = int(input("a: "))
b = int(input("b: "))

if(f(a) * f(b) <= 0):
    print("function root ≈ " + str(bisection(a, b, n_max, graph_values)))
else:
    print("The interval given to the function wont contain any roots, please enter new ones")
    a = int(input("a: "))
    b = int(input("b: "))

print(graph_values)
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()