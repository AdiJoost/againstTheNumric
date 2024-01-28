import numpy as np
import scipy as cp

def main():
    A = np.array([
        [3,4],
        [2,3]
    ])
    singularWertZerlegung(A, chatty=True)

def singularWertZerlegung(A: np.array, matrixName="A", chatty=False):
    U, S, Vt = cp.linalg.svd(A)
    if chatty:
        print(f"Singulärwertzerlegung von {matrixName}")
        print(f"U:\n{U}")
        print(f"S:\n{S}")
        print(f"Vt:\n{Vt}")
    return U, S, Vt

if __name__ == "__main__":
    main()