import numpy as np

def main():
    x = 3
    pr = 3
    x_data = np.array([-1,1,2])
    y_data = np.array([15,5,9])
    y = neAiZero(x_data, y_data)
    print (y)

def neAi(x, x_data, y_data):
    n = np.size(y_data)
    tab = np.block([[y_data], [np.zeros((n-1,n))]])
    for i in range(1,n):
        for j in range(i,n):
            tab[i][j] = ((x-x_data[j-i])*tab[i-1][j]
                         -(x-x_data[j])*tab[i-1][j-1])\
                        /((x_data[j]-x_data[j-i]))
    return tab[n-1][n-1]

def neAiZero(x_data, y_data):
    n = np.size(y_data)
    tab = np.block([[y_data], [np.zeros((n-1, n))]])
    for i in range(1, n):
        for j in range(i,n):
            tab[i][j] = (x_data[j]*tab[i-1][j-1]
                         - x_data[j-i]*tab[i-1][j])\
                         / (x_data[j] - x_data[j-i])
    return tab[n-1][n-1]
            
if __name__ == "__main__":
    main()