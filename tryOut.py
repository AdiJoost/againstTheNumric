import numpy as np
import scipy as cp
import scipy.linalg
from ATNutils.gauss import gaussLgls
from ATNutils.jacobi import jacobi
from ATNutils.richardson import richardson
from ATNutils.auerneumann import auerNeumann

def main():
    A = np.array([
        [1, 0.2, 0.1, 0, 0],
        [0.2, 2, 0.2, 0.1, 0],
        [0.1, 0.2, 3, 0.2, 0.1],
        [0, 0.1, 0.2, 4, 0.2],
        [0,0,0.1,0.2,5]
    ])
    b = np.array([6.85,16.78,29.1,-9.88,29.73])

    #LR Zerlegung
    [p, l , r] = cp.linalg.lu(A)

    with np.printoptions(precision=2):
        print(f"P = \n{p}\n L = \n{l}\n R = \n{r}\n")

    #QR Zerlegung
    [q, r] = np.linalg.qr(A)

    with np.printoptions(precision=2):
        print(f"q = \n{q}\n r = \n{r}\n")

    print(f"Gauss: {gaussLgls(A,b)}")
    print(f"Jacobi: {jacobi(A,b, chatty=False)}")
    print(f"Richardson: {richardson(A, b, chatty=False)}")
    print(f"AuerNeumann: {auerNeumann(A, b)}")



if __name__ == "__main__":
    main()