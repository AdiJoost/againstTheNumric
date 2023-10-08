import numpy as np
import scipy as cp
import scipy.linalg

pr = 2
a = np.array([
                [3,5,0],
                [5,8,-1],
                [2,2,-1]
            ])

[p, l , r] = cp.linalg.lu(a)

with np.printoptions(precision=pr):
    print(f"P = \n{p}\n L = \n{l}\n R = \n{r}\n")