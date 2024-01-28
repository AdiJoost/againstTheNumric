import numpy as np


def main():
    print(newtonRaphson(testF, testFDx, itterations=200000000, chatty=True, startValue=0.56))

def newtonRaphson(f, fDx, startValue=1, tol=10**-16, itterations=100, chatty=True):
    x = startValue
    for i in range(itterations):
        f_x = f(x)
        fDx_x = fDx(x)
        if fDx_x == 0:
            print("Failed due to fDx = 0")
            return
        xNext = x - f_x/fDx_x

        if chatty:
            _printItteration(x, f_x, fDx_x, xNext, i)

        if(np.abs(x - xNext) < tol):
            return x

        x = xNext
    return x
        


def _printItteration(x, f_x, fDx_x, xNext, i):
    print(f"------ Itteration {i} ------")
    print(f"--- x{i} ---\n{x}")
    print(f"--- f_x{i} ---\n{f_x}")
    print(f"--- fDx_x{i} ---\n{fDx_x}")
    print(f"Error: {xNext- x}")

def testF(x):
    return np.exp(-x) - x

def testFDx(x):
    return -np.exp(-x) - 1

if __name__ == "__main__":
    main()