import numpy as np
import scipy as cp
import scipy.linalg

pr = 2
a = np.array([
    [3,1],
    [6,9]
])
[q, r] = np.linalg.qr(a)

with np.printoptions(precision=pr):
    print(f"q = \n{q}\n r = \n{r}\n")