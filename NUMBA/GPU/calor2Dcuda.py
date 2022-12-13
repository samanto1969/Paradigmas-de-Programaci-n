import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *

# ========================================================================
# Numero de celdas
n = np.array([512,512],dtype=np.int64)
# Tamaño de dominio (menor que uno)
L = np.array([1.0,1.0],dtype=np.float64)
# Constante de difusion
kd:float64 = 0.2
# Pasos de tiempo
pasos:int = 1000
# -----------------------------------------------------------------------

# Tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# Paso de tiempo
dt = 0.25*(min(dx[0],dx[1)]**2)/kd
print("dt = ",dt)
