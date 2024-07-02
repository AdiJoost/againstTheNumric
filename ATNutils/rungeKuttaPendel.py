import numpy as np
import matplotlib.pyplot as plt

def main():
    initialVector = np.array([np.pi / 4, 0])
    xPoints, yVector = rungeKuttaSystem(_f, 0, initialVector, 2, 100, 12)
    plotWinkel(xPoints, yVector)
    plotFunction(xPoints, yVector[:,0])
    plt.title("phi(t) : Phasenwinkel zum Zeitpunkt t")
    plt.xlabel("Time in Sekunden")
    plt.ylabel("Phi in rad")
    plt.show()
    plotFunction(xPoints, yVector[:,1])
    plt.title("w(t) : Winkelgeschwindigkeit zum Zeitpunkt t")
    plt.xlabel("Time in Sekunden")
    plt.ylabel("Winkelgeschwindigkeit in m*s")
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
    g = 9.81
    l= 0.88
    returnVector = np.zeros(y.shape)
    returnVector[0] = y[1]
    returnVector[1] = -(g / l) *np.sin(y[0])
    return returnVector

def plotFunction(x, y):
    plt.plot(x,y)

def plotWinkel(x, y):
    plt.plot(x, y[:,0], label="Phasenwinkel phi")
    plt.plot(x, y[:,1], label="Winkelgeschwindigkeit Omega")
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()