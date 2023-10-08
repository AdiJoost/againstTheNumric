import numpy as np

def main():
    a = np.array([
        [10,1,2],
        [3,10,2],
        [3,1,10]
    ])
    b = np.array([13, 15, 14])
    x = richardson(a,b, s=0.1)
    print(x)

def richardson(a, b, s=0.22, N=100, pr_x=3, chatty=True):
    n = np.shape(b)[0]

    h = s*np.eye(n)
    m = np.eye(n) - h@a
    q = h@b
    x = b
    w = 0
    k = 0

    def f(x): 
        y = m@x + q
        return y

    while np.array_equal(x,w) == False and k < N:
        w = x
        k = k + 1
        x = f(x)
        if(chatty):
            print(f"x_{k} = {x}")

    if(chatty):
        print(f"Lösung: x = {np.array2string(x, precision=pr_x)}")
    return x

if __name__ == "__main__":
    main()