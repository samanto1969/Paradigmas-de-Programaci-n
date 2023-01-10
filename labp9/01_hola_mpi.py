#==================================================================
#   INSTITUTO POLITECNICO NACIONAL
#   ESCUELA SUPERIOR DE FÍSICA Y MATEMÁTICAS
#   MATERIA:     PARADIGMAS DE PROGRAMACIÓN
#   PROFESOR:    DOCTOR BECERRA SAGREDO JULIAN TERCERO
#   GRUPO:       2AV1
#   ALUMNO:      FERNANDO NICASIO RAMÍREZ
#   FECHA:       11 DE ENERO DE 2023
#===================================================================
#
#




#===============================
# mpiexc -n python3 hola_mpi.py
# mpirun -n python3 hola_mpi.py
#===============================
# Para correr en 3 procesos
#===========================

from mpi4py import MPI

#=============================
# Crear un objeto comunicador
#=============================

comunicadores = MPI.COMM_WORLD

#==========================
# Numero total de procesos
#==========================

n_procesos = comunicadores.Get_size()

#=========================================
# Numero identificador de de este proceso
#=========================================

quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), "de", str(n_procesos))


