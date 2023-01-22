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
#   PROGRAMA:       02_multi.py
#
#=====================================================================

from multiprocessing import Process
import os 
import math
import time

def calc():
    for i in range(0, 4000000):
        math.sqrt(i)

procesos = []
cpus = os.cpu_count()
print("Nucleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join()

end = time.time()
print("Se tardó: ", end-start)


