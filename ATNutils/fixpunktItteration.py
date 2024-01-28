import numpy as np

def main():
    fixpunktItteration(0.1, _testItteration,)

def fixpunktItteration(x, fx, tol=10**-16, itterations=100, chatty=True):
    for i in range(itterations):
        xNext = fx(x)
        if chatty:
            _printItteration(x, xNext, i)
        if (np.abs(x - xNext) < tol):
            return x
        x = xNext
    return x

def _printItteration(x, xNext, i):
    print(f"------ Itteration {i} ------")
    print(f"x{i}: {x}")
    print(f"x{i}+1: {xNext}")

def _testItteration(x):
    return np.exp(-x)

if __name__ == "__main__":
    main()