import numpy as np

def main():
    x_data = np.array([-1,1,2])
    y_data = np.array([15,5,9])
    c_data = newtons(x_data, y_data)
    print(c_data)

def newtons(x_data, y_data,N=10, lw=3):
    x_0 = x_data[0]
    x_e = x_data[-1]


    n = np.size(y_data)
    tab = np.block([
        [y_data],
        [np.zeros((n-1, n))]
    ])

    c_data = np.zeros(n)
    c_data[0] = y_data[0]
    for i in range(1,n):
        for j in range(i,n):
            tab[i][j] = (tab[i-1][j] - tab[i-1][j-1]) / (x_data[j] - x_data[j-i])
        c_data[i] = tab[i][i]
    return c_data

if __name__ == "__main__":
    main()