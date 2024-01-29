import numpy as np
from moorePenrosePseudoinvers import moorePenrosePseudoInverse


def main():
    #print(newtonRaphson(testF, testFDx, startValues=(-10,-5,0, 5, 10), itterations=1000000, chatty=False, tol=0))
    print(newtonRaphsonNDimensional(testNF, testNFJacobi, startValues=((0.5,0.7),)))

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

def newtonRaphsonNDimensional(fx, jacobiMatrixF, startValues, itterations=100, chatty=True, tol=10**-16):
    """
    returns a list of vectors xi, where fx(xi) = 0
    fx is a ndimensional function where f(x) is a python function with an input of an array and an output of an array,
    jacobiMatrixF is the Jacobi Matrix of fx, a python function with an input of an array and an output of a Matrix
    """
    returnValues = []
    for startValue in startValues:
        x = startValue
        for i in range(itterations):
            f_x = fx(x)
            J_x = jacobiMatrixF(x)
            delta_x = _solve(f_x, J_x)
            xNext = x - delta_x

            if chatty:
                print(f"------ Itteration {i} ------")
                print(f"--- x{i} ---\n{x}")
                print(f"--- f_x{i} ---\n{f_x}")
                print(f"--- J_X{i} ---\n{J_x}")
                print(f"Delta x: {delta_x}")
                print(f"Error: {xNext- x}")

            if (np.allclose(x, xNext, tol)):
                returnValues.append(x)
                break
            x = xNext
        returnValues.append(x)
    return returnValues


def _printItteration(x, f_x, fDx_x, xNext, i): 
    print(f"------ Itteration {i} ------")
    print(f"--- x{i} ---\n{x}")
    print(f"--- f_x{i} ---\n{f_x}")
    print(f"--- fDx_x{i} ---\n{fDx_x}")
    print(f"Error: {xNext- x}")

def _solve(f_x, J_x):
    return moorePenrosePseudoInverse(J_x, f_x, tuner = 0.00001)

def testF(x):
    return x**3 - x**2 - x + 1

def testFDx(x):
    return 3*x**2 -2*x - 1

def testNF(x):
    f_x = np.array([0.0,0.0])
    f_x[0] = np.cos(x[0]) - x[1]
    f_x[1] = -np.sin(x[1]) - x[0]
    return f_x

def testNFJacobi(x):
    J_x = np.array([
        [0.0,0.0],
        [0.0,0.0]
    ])
    J_x[0,0] = -np.sin(x[0])
    J_x[0,1] = -1
    J_x[1,0] = -1
    J_x[1, 1] = -np.cos(x[1])
    return J_x

if __name__ == "__main__":
    main()