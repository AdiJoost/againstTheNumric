import numpy as np


def main():
    x = newtonRaphson(F, fDx, startValues=(0, 0.5, 1, 2, 3, 4))
    print("_________Solutions_________")
    print(x)

def newtonRaphson(f, fDx, startValues=(1), tol=10**-16, itterations=100, chatty=True):
    """
    retruns a list of xi, where f(xi) = 0
    
    """
    returnValues = []
    for startValue in startValues:
        x = startValue
        for i in range(itterations):
            f_x = f(x)
            fDx_x = fDx(x)
            if fDx_x == 0:
                print(f"\n StartValue {startValue} Failed due to fDx = 0")
                break
            xNext = x - f_x/fDx_x

            if chatty:
                _printItteration(x, f_x, fDx_x, xNext, i)

            if(np.abs(x - xNext) < tol):
                returnValues.append(x)
                break

            x = xNext

            if(i == itterations - 1):
                returnValues.append(x)
    
    return set(returnValues)

def _printItteration(x, f_x, fDx_x, xNext, i): 
    print(f"------ Itteration {i} ------")
    print(f"--- x{i} ---\n{x}")
    print(f"--- f_x{i} ---\n{f_x}")
    print(f"--- fDx_x{i} ---\n{fDx_x}")
    print(f"Error: {xNext- x}")

def F(x):
    return 2*x * np.sin(0.5*np.pi + x) - 1

def fDx(x):
    return 2* np.sin(0.5*np.pi + x) + 2*x *np.cos(0.5*np.pi + x)

if __name__ == "__main__":
    main()