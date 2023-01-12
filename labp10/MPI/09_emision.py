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
#   PROGRAMA:       09_emision.py
#
#=====================================================================
#   Broadcast com MPI
#   distribución de datos
#=====================================================================
from mpi4py import MPI

#   Objeto comunicador
comm = MPI.COMM_WORLD

#   Quien soy
rank = comm.Get_rank()

#======================================================================
#   El proceso 0 tiene datos y los otros no
#======================================================================
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3],
            'key2' : ('abc', 'xyz')}

else:
    data = None

#=====================================================================
#    Enviar diccionario a todos los procesos desde root
#=====================================================================
data = comm.bcast(data, root=0)
print(data)


