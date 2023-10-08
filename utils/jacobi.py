import numpy as np

def main():
    a = np.array([
        [10,1,2],
        [3,10,2],
        [3,1,10]
    ])
    b = np.array([13,15,14])
    x = jacobi(a, b)
    print(x)

def jacobi(a, b, N=100, pr_x=3, pr_y=2, pr_t=16, chatty=True):

    n = np.shape(b)[0]

    h = np.diag(1/np.diag(a))
    m = np.eye(n) - h@a
    y = np.linalg.norm(m)

    q = h@b
    x = b
    w = 0
    k = 0

    def f(x):
        y = m@x + q
        return y

    while np.array_equal(x, w) == False and k < N:
        w = x
        k = k+1
        x = f(x)
        if(chatty):
            print(f"x_{k}: {np.array2string(x, precision=pr_x)}")

    if(chatty):
        print(f"Lösung: x = {np.array2string(x, precision=pr_x)}")
    return x

if __name__ == "__main__":
    main()