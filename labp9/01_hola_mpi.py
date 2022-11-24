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

quien_soy = comunicadoress.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), "de", str(n_procesos))


