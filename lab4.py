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
        #   variable de la estrudtura completa llanta
        Llanta.cuenta += 1
        #   variable exclusivas de cado objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión
    
    #===========================================================
    #   Objetos (instanciados)
    #===========================================================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)
    

#==========================================================
#   Objeto que contiene otros objetos
#==========================================================
class Coche:
   def __init__(mi,ll1,ll2,ll3,ll4):
            mi.llanta1 = ll1
            mi.llanta2 = ll2
            mi.llanta3 = ll3
            mi.llanta4 = ll4
    
micoche = Coche(llanta1,llanta2,llanta3,llanta4)
print("Total de llantas: ",Llanta.cuenta)  #Variable global de la clade
print("Presión de la llanta 4 = ", llanta4.presión) #Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presión)

#=================
#   Encapdulamiento
#==================

#==============================================================================
#   Uso de la función de python property para poner y poner y obtener atributos
#===============================================================================
class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obtener_nombre')
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)

#=================================================
#   Crear objeto estudiante sin nombre
#=================================================
estudiante = Estudiante()

#=================================================================================
#   Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
#   (sin tener que llamar explícitamente la función)
#=================================================================================
estudiante.nombre = "Diego"

#================================================================================
#   Obtener el nombre con el método obtener_nombre
#   __nombre es una variable encapsulada (no visible desde fuera)
#   (sin tener que llamar explícitamente a la función obtener_nombre)
#================================================================================
print(estudiante.nombre)

#   Esto no funciona
#   print(estudiante.__nombre)

#================================================================================
#   Herencia de clases
#================================================================================
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d
    
    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro=",p)
        return p

#==============================================================
#   Su hijo rectángulo
#   Rectángulo es hijo de Cuadrilátero
#   Rectangulo(Cuadrilatero)
#==============================================================
class Rectangulo(Cuadrilatero):
    def __init__(self,a,b):
        #====================================
        #   Constructor de su madre
        #====================================
        super().__init__(a,b,a,b)

#===============================================================
#   Su nieto Cuadrado
#   Hijo de Rectángulo
#===============================================================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

    #def perimetro(self).
    #   p = 4.0*self.lado1
    #   print("perimetro = ",p)
    #   return p

#=================================================================
#   Crear un Cuadrado
#=================================================================
cuadrado1 = Cuadrado(5)

#=================================================================
#   Llamar al método perímetro de su abuelo Cuadrilatero
#=================================================================
perimetro1 = cuadrado1.perimetro()

#================================================================
#   Llamar a su propio método área
#===============================================================
areal = cuadrado1.area()

print("Perímetro = ", perimetro1)
print("Área = ", areal)

#===============================================================
#   La clade A tiene tres números reales
#===============================================================
class A:
    __a:float=0.0
    __b:float=0.0
    __c:float=0.0

    def __init__(self,a:float,b:float,c:float):
        self.a = a
        self.b = b
        self.c = c

#===============================================================
#   La clase B tiene dos números reales
#==============================================================
class B:
    __d:float=0.0
    __e:float=0.0

    def _init__(self,d:float,e:float):
        self.d = d
        self.e = e

    #=======================================================
    #   Método sumar todo (internos + externos)
    #=======================================================

    def sumar_todo(self,aa:float,bb:float):
        x:float=self.d+self.e+aa+bb
        return x

#============================================================
#   ASOCIACIÓN
#===========================================================
#   Usando objetos independientes
objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)

print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#============================================================
#   El objeto C tiene dos reales y un objeto A
#   El objeto A se instanci dentro de C
#===========================================================
class C:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        #   A está instanciado adentro
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x

#================================================================
#   COMPOSICIÓN
#   Contiene otro objeto dentro
#================================================================
objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())

#================================================================
#   Objeto D tiene dos reales y un objeto A
#   definido por fuera
#================================================================
class D:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float,Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x

#=================================================================
#   AGREGACIÓN
#   Construye el objeto agregado por fuera
#=================================================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())




