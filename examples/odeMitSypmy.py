import sympy as sp


def main():
    x = sp.symbols('x')
    y_1 = sp.Function('y_1')
    y_2 = sp.Function('y_2')

    eqs = [
            sp.Eq(
                y_1(x).diff(x), 2 * y_1(x)
                ),
            sp.Eq(
                y_2(x).diff(x), 3*y_2(x)
            )]

    L=sp.solvers.ode.systems.dsolve_system(eqs)
    print(L)

if __name__ == "__main__":
    main()