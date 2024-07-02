import numpy as np
import matplotlib.pyplot as plt


def calculatePoly(xData, yData, degree):
    p=np.polyfit(xData, yData, degree)
    newData = np.polyval(p, xData)
    fig, ax = plt.subplots()
    ax.scatter(xData, yData, color="blue")
    ax.plot(xData, newData, color="green")
    plt.show()
    


xData = np.array([1,2,3,4,5,6,7])
yData = np.array([2.5,2.2,1.5,1.0,0.6,-0.3,-1.4])

xData2 = np.array([-2,0,2,4,6,8,10])
yData2 = yData2 = np.array([0.5,0.4,1.1,1.8,3.5,3.0,4.2])


