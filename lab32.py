#==============================================================================
#   Primera Función
#==============================================================================

def saludo():

    #======================================================================
    #   Documentación rápida de la fución
    #======================================================================

    """Esta función salida"""
    print('¡Quiúbules!, ¿Cómo estás?')
     
#==============================================================================
#   Llamado de la función
#==============================================================================

saludo()


#==============================================================================
#   Se ejecuta pero no se asigna
#==============================================================================
salida = saludo()

#=============================================================================
#   Esto no funciona
#=============================================================================
print(salida)

#============================================================================
#   Mostrar documentación
#============================================================================
#help(saludo)


#===========================================================================
#  Función con argumento
#===========================================================================
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Qué onde ese", nombre, "!")
salu2("Julian")
salu2("Ángel")

#============================================================================
#   Ahorrar trabajo del intérprete
#   nombre:str la variable nombre es un str
#============================================================================
def saludos(nombre:str):
    """Esta función te saludda por tu nombre edtrictamente"""
    print("¡Qué inda ese",nombre,"!")
saludos("Julián")
a = 123
print(type(a))
saludos(a)
#====================================================================
#   Función con muchos argumentns
#=====================================================================
def saludos_multiples(nombre, nombre2,nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1,"'",nombre2, "y",nombre3)
saludos_multiples("Hugo","Paco","Luis")
#======================================================================
#   Función con cualquier número de argumentos
#=======================================================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los sque quieras"""
    i = 0
    #==================================================
    #   end= es para ponerlo de corrido
    #==================================================
    print("Hola", end="")
    while len(nombres) > i:
        # Último nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else
           # Cualquier otro nombre
           print(nombres[i], end==",")
        i+=1
muchos_saludos("Bosco","Ángel","David","Tamara","Mili","Edwin","Lev","Luis","Abigail")
def greet(firsrname, lastname):
#=============================================================
#   Llamar la función con argumentos en desorden
#===========================================================
greet(lastname='Jobs',firstname='Steve') # Se pueden especificar las varibles en desorden
#==============================================================
#   Función co argumentos escondidos
#==============================================================
def greet(**person):
    #===============================================
    #   persona tiene caraterísticas firstname y lastname
    #=====================================================
    print('Helo', person['firstname'],person['lastname']
greet(firstname='Steve',lastname='Jobs')
greet(lastname='Jobs',firstmame='Steve')
greet(firstname='Bill',lastname='Gates') # Se pueden pasar más parámetros de los necesarios
#============================================================================================
#   Función con valores por defecto
#============================================================================================
def greet(name = 'Guest'):
    print('Hello',name)

greet() # Utiliza el valor dado de antemano
greet('Steve')
#=============================================
#   Función resultado
#==============================================
def suma(a, b):
    return a+b
#==============================================
#   Se pueden funciones en funciiones
#==============================================
total=suma(5, suma(10, 20))
print(total)
#===============================================
#   Cálculo lambda
#   nombre de la función = lambda variable : función
#===================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)
#===================================================
#   Lambda de varias variables
#==================================================
suma = lambda x1,x2,x3: x1+x2+x3
print(suma(99,98,97))

sumas=lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))
#========================================================
#   Uso de una función anónima
#   El argumento va afuera entre paréntesis
#==========================================================
print((lambda x: x*x)(6)) # Función anónima
#===========================================================
#   Función con variable global
#   EVITE EL EXCESO !!!!
#==========================================================
name = 'Steve'
def greet():
    global name # Para utilizar una variable global (que viene fuera del bloque)
    name = 'Bill'
    print('Hello',name)

greet()


#==============================================================
#==============================================================

#                        Algoritmo 1

#==============================================================
#===============================================================
#   Serie Exponencial
#   Factorización de x
#   Negativos con función inversa
#===============================================================
n = 200
x = -100.0
flag = False
if x<0:
    flag = True
    x = -x
s = 1.0
for i in range(n,0,-1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s = 1/s
print(s)





















































