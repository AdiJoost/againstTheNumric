import numpy as np


def main():
    print(newtonRaphson(testF, testFDx, startValues=(-10,-5,0, 5, 10), itterations=1000000, chatty=False, tol=0))

def newtonRaphson(f, fDx, startValues=(1), tol=10**-16, itterations=100, chatty=True):
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

def testF(x):
    return x**3 - x**2 - x + 1

def testFDx(x):
    return 3*x**2 -2*x - 1

if __name__ == "__main__":
    main()