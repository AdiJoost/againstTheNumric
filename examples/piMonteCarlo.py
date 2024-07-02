import numpy as np
from tqdm import tqdm

def main():
    numbersOfShots = 100000000
    hits = 0
    N = 1
    for i in tqdm(range(numbersOfShots)):
        randomX = np.random.rand()
        randomY = np.random.rand()
        if isHit(randomX, randomY):
            hits += 1
    
    a = 4*hits/numbersOfShots
    print(a)

def isHit(x, y):
    return np.sqrt(x**2 + y**2) < 1

if __name__ == "__main__":
    main()