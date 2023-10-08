import numpy as np
import scipy as cp
import scipy.linalg
from hilbermatrix import getHilbertMatrix

def main():
    A, B = getHilbertMatrix(100)
    print(mPPI(A,B))
    print(betterMppI(A,B))

def mPPI(A, B, tuner = 0.1):
    S = np.zeros(A.shape)
    [U, SDiag, Vt] = cp.linalg.svd(A)
    np.fill_diagonal(S, SDiag)
    x = Vt.T@np.linalg.inv(S)@U.T@B
    return x

def betterMppI(A, B, tuner=0.1):
    Ap = cp.linalg.pinv(A, tuner)
    x = Ap@B
    return x
    

if __name__ == "__main__":
    main()