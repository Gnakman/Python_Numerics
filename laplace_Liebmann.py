import numpy as np
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

lx = 1
ly = 1
nx = 41
ny = 41
dx = lx/(nx-1)
dy = ly/(ny-1)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

p = np.ones([nx,ny])
p[:,0] = 0
p[:,-1] = 2
p[0,:] = 2
p[-1,:] = 2

p_temp = p.copy()
target_norm = 0.005
norm = 2
#for k in range(6):
while norm > target_norm: 
    p_temp = p.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            p[i,j] = (dy**2*(p[i+1,j]+p[i-1,j])+dx**2*(p[i,j+1]+p[i,j-1]))/(dx**2+dy**2)/2
            norm = (np.linalg.norm(p)-np.linalg.norm(p_temp))/np.linalg.norm(p_temp)
            
            

# Luckliy the matrix is always diagonally dominant 


fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, p, cmap=cm.viridis, rstride=1, cstride=1)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
pyplot.show()
