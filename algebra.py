from sympy.solvers import solve
from sympy import Symbol
from math import e, sqrt

x = Symbol('x')
sol = solve(x+5 - 5/8)
print(sol)