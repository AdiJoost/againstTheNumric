import numpy as np


def main():
    A = np.array([
        [10,1,2],
        [3,10,2],
        [3,1,10]
    ])

    b = np.array([13,15,14])
    print(auerNeumann(A, b))

def auerNeumann(A, b, N=100, pr_x=3, pr_y=2, pr_t=16, chatty=True):
    n = np.shape(b)[0]
    D = np.diag(1 / np.diag(A))
    B = D@A
    C = np.eye(n) - B
    H = np.eye(n) + C
    M = np.eye(n) - H@B
    y = np.linalg.norm(M)
    if (chatty):
        print(f"Norm of M: {y :#.{ pr_y }g}")

    q= H@D@b
    x=q
    w=0
    k=0
    while np.array_equal(x,w) == False and k < N:
        w=x
        k += 1
        x = auerNeumannItteration(x, M, q)
        if(chatty):
            print ( f"x_{k} = {np. array2string (x, precision = pr_t )}")
    
    return x

def auerNeumannItteration(x, M, q):
    return M@x + q
    

if __name__ == "__main__":
    main()