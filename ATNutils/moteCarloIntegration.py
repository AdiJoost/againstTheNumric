import numpy as np
from tqdm import tqdm

def main():
    #print(monteCarloIntegration(_f, -1, 1, 2, 1000000))
    #print(monteCarlo2DIntegration(_fD2, 0, 1, 0, 2, 4, 100000))
    print(monteCarloVolumen((isInSphere, isInXylinder), -2, 2, -2, 2, -2, 2, 10000000))

def monteCarloIntegration(f, x0, xEnd, maxY, numberOfShots):
    hits=0
    for i in tqdm(range(numberOfShots)):
        randomX = np.random.uniform(x0, xEnd)
        randomY = np.random.uniform(0, maxY)
        if randomY < f(randomX):
            hits += 1
    
    return (hits / numberOfShots) * (xEnd - x0) * maxY 

def monteCarlo2DIntegration(f, x0, xEnd, y0, yEnd, maxZ, numberOfShots):
    hits=0
    for i in tqdm(range(numberOfShots)):
        randomX = np.random.uniform(x0, xEnd)
        randomY = np.random.uniform(y0, yEnd)
        randomZ = np.random.uniform(0, maxZ)
        if randomZ < f(randomX, randomY):
            hits += 1
    
    return (hits / numberOfShots) * (xEnd - x0) * (yEnd - y0) * maxZ

def monteCarloVolumen(fD, x0, xEnd, y0, yEnd, z0, zEnd, numberOfShots):
    hits = 0
    for i in tqdm(range(numberOfShots)):
        randomX = np.random.uniform(x0, xEnd)
        randomY = np.random.uniform(y0, yEnd)
        randomZ = np.random.uniform(z0, zEnd)
        isHit = True
        for function in fD:
            if not function(randomX, randomY, randomZ):
                isHit = False
        if isHit:
            hits += 1

    return (xEnd - x0) * (yEnd - y0) * (zEnd - z0) * (hits / numberOfShots)



def _f(x):
    return 1 / (1 + np.abs(x))

def _fD2(x, y):
    return 3 / (1 + x**2 + y ** 2)

def isInSphere(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2) < 2

def isInXylinder(x, y, z):
    return np.sqrt(x ** 2 + (z - 1) ** 2) < 1


if __name__ == "__main__":
    main()