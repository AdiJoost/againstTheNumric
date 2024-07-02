import numpy as np

def main():
    a = np.array([
        [2,1,0,2],
        [4,2,3,3],
        [-2,-1,6,-4],
        [-8,-4,9,-11],
        [2,1,-3,3]
    ])
    b = np.array([6,16,2,-12,2])
    pr = 3
    x = gaussLgls(a,b)
    print(x)

def gaussLgls(a, b):
    g = 1.0 * np.block([a, np.expand_dims(b, axis=1)])
    n = a.shape[0]

    for ps in range (0 ,n-1):
        mm = ps+np.argmax(np.abs(g[range(ps,n), ps]))
        if mm != ps:
            tmp = np.copy(g[ps])
            g[ps] = g[mm]
            g[mm] = tmp
            p = g[ps][ps]
            for zz in range (ps+1, n):
                f = g[zz][ps] / p
                g[zz][ps] = 0.0
                for ss in range(ps+1, n+1):
                    g[zz][ss] = g[zz][ss] - f*g[ps][ss]
    x = np.zeros(n)
    w = 0
    for rr in range(n-1, -1, -1):
        for ss in range(n-1, rr, -1):
            w = x[ss] * g[rr][ss]
        x[rr] = (g[rr][-1] - w) / g[rr][rr]
    return x


if __name__ == "__main__":
    main()