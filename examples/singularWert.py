import numpy as np
import scipy as cp
import scipy.linalg

def main():
    matrix = np.array([
        [2,0],
        [0,3]
    ])
    U, S, Vt = cp.linalg.svd(matrix)
    print(f"U:\n{U}")
    print(f"S:\n{S}")
    print(f"Vt:\n{Vt}")


if __name__ == "__main__":
    main()