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
#   PROGRAMA:       011_colectar.py
#
#=====================================================================
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2

#=====================================================================
#   Manden sus datos al proceso root=0
#   (en orden)
#=====================================================================
datas = comm.gather(data, root=0)

#=====================================================================
#   Asegurarse que todo funcione
#=====================================================================
if rank == 0:
    for i in range(size):
        assert datas[i] == (i+1)**2
else:
    assert datas is None

print(datas)

