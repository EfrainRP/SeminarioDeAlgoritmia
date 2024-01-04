
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y=38*x**3+6*x**2+11*x+78
    return y

def fPrima(x):
    return 114*x**2+12*x+11

def fPrima2(x):
    return 228*x+12

t=np.arange(-1,1,0.00001)
plt.figure()

plt.subplot(1,3,1)
plt.plot(t,f(t),'k')
plt.title("F(x) = 38x^3+6x^2+11x+78")

plt.subplot(1,3,2)
plt.plot(t,fPrima(t),'m')
plt.title("F'(x) = 114x^2+12x+11")

plt.subplot(1,3,3)
plt.plot(t,fPrima2(t),'g')
plt.title("F''(x) = 228x+12")

plt.show()
