import numpy as np
import scipy as cp
import scipy.linalg

def main():
    from hilbermatrix import getHilbertMatrix
    A, B = getHilbertMatrix(100)
    print(mPPI(A,B))
    print(moorePenrosePseudoInverse(A,B))

def mPPI(A, B, tuner = 0):
    S = np.zeros(A.shape)
    [U, SDiag, Vt] = cp.linalg.svd(A)
    np.fill_diagonal(S, SDiag)
    SInverse = np.linalg.inv(S)
    if(tuner != 0):
        SInverse[SInverse > 1 / tuner] = 0
    #x = V * S**-1 * Ut * b
    x = Vt.T @ SInverse @ U.T @ B
    return x

def moorePenrosePseudoInverse(A, B, tuner=0.1):
    Ap = cp.linalg.pinv(A, tuner)
    x = Ap@B
    return x
    

if __name__ == "__main__":
    main()