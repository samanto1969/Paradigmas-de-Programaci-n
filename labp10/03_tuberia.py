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
#   PROGRAMA:       03_tuberias.py
#
#=====================================================================

from multiprocessing import Process, Pipe

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)

if __name__ == "__main__":
    extremo1, extremo2 = Pipe()
    proceso1 = Process(target=f, args=(extremo1,))
    proceso2 = Process(target=g, args=(extremo2,))
    proceso2.start()
    proceso1.start()
    proceso1.join()
    proceso2.join()


