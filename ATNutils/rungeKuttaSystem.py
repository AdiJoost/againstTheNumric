import numpy as np
import matplotlib.pyplot as plt

def main():
    initialVector = np.array([-1, 1])
    xPoints, yVector = rungeKuttaSystem(_f, 2, initialVector, 2, 100, 12)
    plotFunction(xPoints, yVector[:,0])
    plotFunction(xPoints, yVector[:,1])
    plt.show()

def rungeKuttaSystem(f, x0, y0, numberOfEquations, numberOfPoints, xEnd):
    xPoints = np.linspace(x0, xEnd, numberOfPoints)
    yVector = np.zeros((xPoints.shape[0], numberOfEquations))
    xPoints[0] = x0
    yVector[0,:] = y0
    stepSize = xPoints[1] - xPoints[0]

    for i in range(xPoints.shape[0] - 1):
        k1 = f(xPoints[i], yVector[i,:]) * stepSize
        k2 = f(xPoints[i] + stepSize/2, yVector[i,:] + k1/2) * stepSize
        k3 = f(xPoints[i] + stepSize/2, yVector[i,:] + k2/2) * stepSize
        k4 = f(xPoints[i+1], yVector[i,:] + k3) * stepSize

        yVector[i + 1,:] = yVector[i,:] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    return xPoints, yVector

def _f(x, y):
    returnVector = np.zeros(y.shape)
    returnVector[0] = y[1] * np.cos(3*x) + np.exp(-x)
    returnVector[1] = y[0] * np.sin(3*x) + np.exp(-x)
    return returnVector

def plotFunction(x, y):
    plt.plot(x,y)

if __name__ == "__main__":
    main()