#this is first order
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def hiv(x,t):
    kr1 = 1e5
    kr2 = 0.1
    kr3 = 2e-7
    kr4 = 0.5
    kr5 = 5
    kr6 = 100

    h = x[0]
    i = x[1]
    v = x[2]
    p = kr3*h*v
    dhdt = kr1-kr2*h-p
    didt = p-kr4*i
    dvdt = -p-kr5*v+kr6*i
    return[dhdt,didt,dvdt]

x0 = [1e6,0,100]
t = np.linspace(0,15,1000)
x = odeint(hiv,x0,t)

h = x[:,0]
i = x[:,1]
v = x[:,2]

plt.plot(t,h)

