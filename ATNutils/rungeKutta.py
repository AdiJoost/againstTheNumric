import numpy as np
import matplotlib.pyplot as plt

def main():
    xEuler, yEuler = rungeKutta(_f, 2, 9, numberOfPoints=10000, xEnd=10)
    plotFunction(xEuler, yEuler)
    plt.show()

    x, y = cauchyRichardsonFolge(_f, 2, 9, startNumberOfPoints=50, xEnd=10, itterations=10)
    plotCauchyRichardsonFolge(x,y)
    plt.show()

def rungeKutta(f, x0, y0, numberOfPoints, xEnd):
    xPoints = np.linspace(x0, xEnd, numberOfPoints)
    yPoints = np.zeros(xPoints.shape[0])
    xPoints[0] = x0
    yPoints[0] = y0
    stepSize = xPoints[1] - xPoints[0]

    for i in range(xPoints.shape[0] - 1):
        k1 = f(xPoints[i], yPoints[i]) * stepSize
        k2 = f(xPoints[i] + stepSize/2, yPoints[i] + k1/2) * stepSize
        k3 = f(xPoints[i] + stepSize/2, yPoints[i] + k2/2) * stepSize
        k4 = f(xPoints[i+1], yPoints[i] + k3) * stepSize

        yPoints[i + 1] = yPoints[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    return xPoints, yPoints

def cauchyRichardsonFolge(f, x0, y0, startNumberOfPoints, xEnd, itterations):
    numberOfPointsArray = np.zeros(itterations)
    maxDifferencesArray = np.zeros(itterations)
    _, yPoints = rungeKutta(f, x0, y0, startNumberOfPoints, xEnd)
    for i in range(1, itterations):
        numberOfPointsInItteration = startNumberOfPoints * 2**i
        _, newYPoints = rungeKutta(f, x0, y0, numberOfPointsInItteration, xEnd)
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