import numpy as np
import scipy as cp

def main():
    A = np.array([
        [0,3],
        [0,0]
    ])
    B = cp.linalg.expm(A)
    print(B)


if __name__ == "__main__":
    main()