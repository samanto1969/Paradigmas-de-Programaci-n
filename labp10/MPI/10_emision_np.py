#=====================================================================
#   INSTITUTO POLITECNICO NACIONAL
#   ESCUELA SUPERIOR DE FÍSICA Y MATEMÁTICAS
#   LICENCIATURA:   MATEMÁTICA ALGORÍTMICA
#   MATERIA:        PARADIGMAS DE PROGRAMACIÓN
#   PROFESOR:       DR. BECERRA SAGREDO JULIAN TERCERO
#   GRUPO:          2AV1
#   ALUMNO:         FERNANDO NICASIO RAMÍREZ
#   BOLETA:         2022330153
#
#
#   PROGRAMA:       10_emision_np.py
#
#=====================================================================
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#   Tamaño del arreglo
n = 10
if rank == 0:
    #   Arreglo de enteros del 0 al n-1
    data = numpy.arange(n, dtype='i')
else:
    #   Arreglo vació de enteros de tamaño n
    data = numpy.empty(n, dtype='i')

#=====================================================================
#   Broadcast pro que indica el tipo de dato
#   Optimizado para comunicación rápida
#=====================================================================
comm.Bcast([data,MPI.INT], root=0)

#=====================================================================
#   Asegurarse que toso salió bien
#=====================================================================
for i in range(n):
    assert data[i] == i
print(data)

