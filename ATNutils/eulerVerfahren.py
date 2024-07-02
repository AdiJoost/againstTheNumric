import numpy as np
import matplotlib.pyplot as plt

def main():
    xEuler, yEuler = eulerVerfahren(_f, 2, 9, numberOfPoints=10000, xEnd=10)
    plotFunction(xEuler, yEuler)
    plt.show()

    x, y = cauchyRichardsonFolge(_f, 2, 9, startNumberOfPoints=50, xEnd=10, itterations=10)
    plotCauchyRichardsonFolge(x,y)
    plt.show()
    
def eulerVerfahren(f, x0, y0, numberOfPoints, xEnd):
    xPoints = np.linspace(x0, xEnd, numberOfPoints)
    yPoints = np.zeros(xPoints.shape[0])
    xPoints[0] = x0
    yPoints[0] = y0
    stepSize = xPoints[1] - xPoints[0]
    for i in range(xPoints.shape[0] - 1):
        yPoints[i + 1] = yPoints[i] + f(xPoints[i], yPoints[i]) * stepSize
    
    return xPoints, yPoints

def cauchyRichardsonFolge(f, x0, y0, startNumberOfPoints, xEnd, itterations):
    numberOfPointsArray = np.zeros(itterations)
    maxDifferencesArray = np.zeros(itterations)
    _, yPoints = eulerVerfahren(f, x0, y0, startNumberOfPoints, xEnd)
    for i in range(1, itterations):
        numberOfPointsInItteration = startNumberOfPoints * 2**i
        _, newYPoints = eulerVerfahren(f, x0, y0, numberOfPointsInItteration, xEnd)
        maxDifference = max(np.abs(yPoints - newYPoints[::2]))
        numberOfPointsArray[i] = numberOfPointsInItteration
        maxDifferencesArray[i] = maxDifference
        yPoints = newYPoints
    return numberOfPointsArray, maxDifferencesArray




def _f(x, y):
    return 2*np.sqrt(y)

def plotFunction(x, y):
    plt.plot(x,y)

def plotCauchyRichardsonFolge(x, y):
    plt.loglog(x, y)

if __name__ == "__main__":
    main()