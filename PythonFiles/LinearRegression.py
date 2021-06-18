import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0,10,20,30,40,50,60],[4,111,42,111,234,104,159]])
m, b = np.polyfit(data[0,:], data[1,:],1)
y_ = lambda x_: m*x_ + b

y = y_(25)
plt.vlines(25,0,y,color = "red")
plt.plot([0,25],[y,y],color = "red")

plt.plot(data[0,:], m*data[0,:] + b, color = "aqua", label = "Line of Best Fit")
plt.plot(data[0,:],data[1,:],"o",color = "teal")
plt.plot(25,y,"o", markersize = 5, color = "deeppink", label = "Approximated y at given x")
plt.legend()
plt.show()