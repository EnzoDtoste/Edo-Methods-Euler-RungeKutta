from Fraction import Fraction
from ApproachMethods import Euler, Improved_Euler, Runge_Kutta
import matplotlib.pyplot as plt
from NumString import NumS

def ej18(x, y):
    return x * x - y * y

def ej26(x, y):
    return NumS('0', '0225') * y - NumS('0', '0003') * y * y

def plotear(x, y, h, steps, derivated, method):
    
  xl = [float(str(x))]
  yl = [float(str(y))]

  for i in range(steps):
    
    y = method(x, y, derivated, h)
    yl.append(float(str(y)))

    x += h
    xl.append(float(str(x)))

    print(str(x) + "   " + str(y))

  ax.plot(xl, yl)
  

fig, ax = plt.subplots()

#Descomenta el que quieras probar

#plotear(NumS('0',''), NumS('1',''), NumS('0','0008'), 2500, ej18, Euler)
#plotear(NumS('0',''), NumS('1',''), NumS('0','0008'), 2500, ej18, Improved_Euler)
#plotear(NumS('0',''), NumS('25',''), NumS('1', ''), 1400, ej26, Runge_Kutta)
plt.show()




