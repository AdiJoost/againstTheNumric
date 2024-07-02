import numpy as np
import matplotlib.pyplot as plt

def main():
    xData = np.array([273,412,556,990,1638,1709,3550])
    yData = np.array([976.9,973.6,955.5,902.3,834.2,824.7,649])
    a=2
    yn = yData[0]
    yData = np.log2(yData)
    m, q = calculatePoly(xData,yData, 1)

    epsilon = 1 / m
    yZero =  a **(q + (xData[0]/epsilon))

    print(getPressure(4049, epsilon, yZero, xData[0], a))


def calculatePoly(xData, yData, degree):
    p=np.polyfit(xData, yData, degree)
    newData = np.polyval(p, xData)
    fig, ax = plt.subplots()
    ax.scatter(xData, yData, color="blue")
    ax.plot(xData, newData, color="green")
    plt.show()
    return p

def getPressure(height, epsilon, yZero, xZero, a):
    return yZero * (a **((height-xZero)/ epsilon))

if __name__ == "__main__":
    main()




