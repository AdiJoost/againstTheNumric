import numpy as np
import matplotlib.pyplot as plt


def calculatePoly(xData, yData, degree):
    p=np.polyfit(xData, yData, degree)
    newData = np.polyval(p, xData)
    return p
    fig, ax = plt.subplots()
    ax.scatter(xData, yData, color="blue")
    ax.plot(xData, newData, color="green")
    plt.show()
    
def calcIncome(x, m, q):
    return (x ** 2) *m + x*q


xData = np.array([1.3,1.4,1.5,1.6,1.7])
yData = np.array([17000,15000,14000,13000,11000])

m, q = calculatePoly(xData, yData, 1)
xarrange = np.linspace(0,30, 3000)
yArrange = calcIncome(xarrange, m=m, q=q)
maxIndex = np.argmax(yArrange)
print(xarrange[maxIndex]*m + q)
fig, ax = plt.subplots()

ax.plot(xarrange, yArrange, label="Income")
ax.set_xlabel("EntryPrice")
ax.set_ylabel("Income")

ax.scatter(xarrange[maxIndex], yArrange[maxIndex], label=f"Maximum at {xarrange[maxIndex]}")
ax.legend()
plt.show()
