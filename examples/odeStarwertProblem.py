import sympy as sp

def main():
    x = sp.symbols('x')
    y_1 = sp.Function('y_1')
    y_2 = sp.Function('y_2')

    eqs = [
            sp.Eq(
                y_1(x).diff(x), 3 * y_1(x)
                ),
            sp.Eq(
                y_2(x).diff(x), -5*y_2(x)
            )]
    
    ics= {
        y_1(0): -2,
        y_2(0): -4
    }

    L=sp.solvers.ode.systems.dsolve_system(eqs, ics=ics)
    print(L)

if __name__ == "__main__":
    main()