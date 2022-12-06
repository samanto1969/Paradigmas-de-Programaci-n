import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time


# ==========================================================================
# Número de celdas
n = np.array[512,512])
# Tamaño del dominio (menor que uno)
L = np.array([1.0,1.0])
# Constante de difusión
k = 0.2
# Pasos de tiempo
pasos = 100
# ==========================================================================

# Tamaños de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0],dx[1]**2)/k
print("dt = ", dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ", nt)
# Llenar la solución con ceros
u = np.zeros(nt,dtype=np.float64) # arreglo de lectura
un = np.zeros(nt,dtype=np.float64) # arreglo de escritura

def evolucion(u,n,udx,dt,i,k):
    jp1 = i + n[0]
    jm1 = i + n[0]
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1)]*udx2[0] + (u[jm1]-2.0*u[i]+[jp1])*udx2[1]
    unueva = u[i] + dt*k*laplaciano
    return unueva

def solucion(u,un,udx2,dt,n,k):
    for jj in range(1,n[1]-1):
       for ii in range(1,n[0]-1):


