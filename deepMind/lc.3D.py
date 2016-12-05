import numpy as np  
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import plot,savefig
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
 
fig = plt.figure()  
ax = fig.gca(projection='3d')  
X = np.arange(-5, 5, 0.25)  
Y = np.arange(-5, 5, 0.25)  
X, Y = np.meshgrid(X, Y)  
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)  
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,  linewidth=0, antialiased=False)  
ax.set_zlim(-1.01, 1.01)  
ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
fig.colorbar(surf, shrink=0.5, aspect=5)  
 
plt.show() 
savefig('image.3D.jpg')
