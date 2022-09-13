#====================================================================
#   Fernando Nicasio Ramirez
#   Video 4 de Mitote Ciencia
#===================================================================

#===================================================================
#   PROGRAMACION ORIENTADA A OBJETOS
#===================================================================

#===================================================================
#   Una clase para un objeto vacio
#   No esta tan vacio, necesita
#   la palabra pass = pasar
#==================================================================
class ObjetoVacio:
    pass

#==================================================================
#   nada es ObjetoVacio
#==================================================================
nada = ObjetoVacio()
print(type(nada))
#==================================================================

#==================================================================
#   La clase Llanta
#==================================================================
class Llanta:
    #=============================================================
    #   Variable cuenta es de toda la clase
    #=============================================================
    cuenta = 0

    #=============================================================
    #   Función constructora de identidad 
    #   __init__ es una función reservada 
    #   comienza con uno mismo: self
    #   pero puede ser otro nombre(mi)
    #   parámetros de entrada = default
    #=============================================================
    def __init__(mi, radio=50, ancho=30, presión=1.5):
        #   variable exclusivas de cado objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión




