
import math
import sympy as sp

def main():
    x= sp.symbols('x')
    n = 2
    T = sp.series(sp.log(sp.sqrt(sp.cos(x))), x, 0, n + 1)
    print(T)

def macLaurin(x, f):
    sum = 0
    for i, derivation in enumerate(f):
        sum = derivation(0) * x ** (i) / math.factorial(i)
    return sum

if __name__ == "__main__":
    main()