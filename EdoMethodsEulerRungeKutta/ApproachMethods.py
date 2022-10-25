from Fraction import Fraction
from NumString import NumS

def Euler(x, y, derivated, h):
    return y + h * derivated(x, y)

def Improved_Euler(x, y, derivated, h):

    k1 = derivated(x,y)
    u = y + h * k1
    k2 = derivated(x + h, u)

    return y + h * NumS('0','5') * (k1 + k2) 

def Runge_Kutta(x, y, derivated, h):
    k1 = derivated(x,y)
    k2 = derivated(x + NumS('0', '5') * h, y + NumS('0', '5') * h * k1)
    k3 = derivated(x + NumS('0', '5') * h, y + NumS('0', '5') * h * k2)
    k4 = derivated(x + h, y + h * k3)

    return y + NumS('0', '16666666666666666666667') * h * (k1 + NumS('2') * k2 + NumS('2') * k3 + k4)
