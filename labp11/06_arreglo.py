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
#   PROGRAMA:       06_arreglo.py
#
#=====================================================================

#-----------------------------------------------------------
# Ejemplo de comunicacion bloqueada a un arreglo compartido
# Uso de candados
#-----------------------------------------------------------

from multiprocessing import Process, Array, Lock
import time

def sumale100(numeros,candado):
    for i in range(100):
        time.sleep(0.01)
        #usando candado
        for i in range(len(numeros)):
            # lo que este dentro de con candado no puede accederse
            # desde otro proceso al mismo tiempo
            with candado:
                # hacer la operacion
                numeros[i] +=1

if __name__ == "__main__":
    #-------------------------------------------------
    # Candado para evitar que dos procesos se empalmen
    #-------------------------------------------------

    candado = Lock()

    #Numero comun a los procesos, d de dobles
    numeros_compartidos = Array('d', [0.0, 100.0, 200.0])

    # : quiere decir todos los elementos
    print("Al principio vale = ",numeros_compartidos[:])

    # Dos procesos
    p1 = Process(target=sumale100, args=(numeros_compartidos,candado))
    p2 = Process(target=sumale100, args=(numeros_compartidos,candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numeros_compartidos[:])


