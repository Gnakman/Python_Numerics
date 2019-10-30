import numpy as np
import sys
import xlsxwriter as writer
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(precision=1)

sigma = 0.0009
nu = 0.01
nx  = 41
ny = 41
l_x = 2
l_y = 2
dx = l_x/(nx -1)
dy = l_y/(ny -1)
nt = 120
dt = sigma * dx*dy/nu
x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)


u = np.ones([nx,ny])
v = np.ones([nx,ny])
  
u[int(0.5 / dy):int( 1/dy  + 1),int(0.5 / dx):int(1 / dx + 1)]=2 # have to add 1 since python stops at n-1
v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 # have to add 1 since python stops at n-1

for n in range(1,nt):
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1
    un = u.copy()
    vn = v.copy()
    for i in range(1,nx-1):
        for j in range(1,nx-1):
            u[i,j] = un[i,j] - dt/dx*un[i,j]*(un[i,j]-un[i-1,j]) - dt/dy*vn[i,j]*(un[i,j]-un[i-1,j])+nu*dt/dx/dx*(un[i+1,j]-2*un[i,j]+un[i-1,j])+nu*dt/dy/dy*(un[i+1,j]-2*un[i,j]+un[i-1,j])
            v[i,j] = vn[i,j] - dt/dx*un[i,j]*(vn[i,j]-vn[i,j-1]) - dt/dy*vn[i,j]*(vn[i,j]-vn[i,j-1])+nu*dt/dx/dx*(vn[i,j+1]-2*vn[i,j]+vn[i,j-1])+nu*dt/dy/dy*(vn[i,j+1]-2*vn[i,j]+vn[i,j-1])
            



fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1)
ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');
pyplot.show()
