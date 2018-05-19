import numpy as np
from pylab import  *
import matplotlib.pyplot as plt

vector= np.loadtxt(open("data2.csv", "rb"), delimiter=",", skiprows=1)
coeff1=fft(vector)
p = 20*np.log10(coeff1)
f = np.linspace(0, 10, len(p))
plt.plot(f, p)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Power(dB)")
plt.title("all frequencies")
plt.show() 
