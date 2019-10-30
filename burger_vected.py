import numpy as np
import sys
import xlsxwriter as writer
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(precision=1)


def burger(nt):
    sigma = 0.0009
    nu = 0.01
    nx  = 41
    ny = 41
    l_x = 2
    l_y = 2
    dx = l_x/(nx -1)
    dy = l_y/(ny -1)
    dt = sigma * dx*dy/nu
    x = np.linspace(0, 2, nx)
    y = np.linspace(0, 2, ny)
    u = np.ones([nx,ny])
    v = np.ones([nx,ny])
  
    u[int(0.5 / dy):int( 1/dy  + 1),int(0.5 / dx):int(1 / dx + 1)]=2 # have to add 1 since python stops at n-1
    v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 # have to add 1 since python stops at n-1

    for n in range(nt):
        un =u.copy()
        vn =v.copy()
        u[1:-1,1:-1] = un[1:-1,1:-1] - dt/dx*un[1:-1,1:-1]*(un[1:-1,1:-1]-un[0:-2,1:-1]) - dt/dy*vn[1:-1,1:-1]*(un[1:-1,1:-1]-un[0:-2,1:-1])+nu*dt/dx/dx*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])+nu*dt/dy/dy*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])
        v[1:-1,1:-1] = vn[1:-1,1:-1] - dt/dx*un[1:-1,1:-1]*(vn[1:-1,1:-1]-vn[1:-1,0:-2]) - dt/dy*vn[1:-1,1:-1]*(vn[1:-1,1:-1]-vn[1:-1,0:-2])+nu*dt/dx/dx*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2])+nu*dt/dy/dy*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2])
        # at the end of the day you are solving for (nx -2) points as the boundary conditions are given at the boundaries.
        # u[1:-1,1:-1] is a 39x39 matrix because of this fact. 
    

    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1)
    ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$');
    pyplot.show()


burger(3000)

 
