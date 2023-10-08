import numpy as np

def main():
    A, B = getHilbertMatrix(5)
    print(f"A:\n{A}\nB:\n{B}")

def getHilbertMatrix(n):
    A = np.zeros([n,n])
    B = np.zeros([n])
    for i in range(n):
        for j in range(n):
            A[i,j] = 1 / ((i+1) + j)
            B[i] += 1 / ((i+1) + j)
    return (A, B)

if __name__ == "__main__":
    main()