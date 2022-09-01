#******************************************************************************
#   Fernando Nicasio Ramírez
#   Boleta: 2022330153
#   Grupo: 2AMV
#   Paradigmas de Programación
#******************************************************************************


#*******************************************************************************#   Conjunto en python
#*******************************************************************************

even_nums = {2.4. 6, 8, 10}  # conjunto de números pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10,5 True } # conjunto de diferente objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)


#*******************************************************************************
#   Convertir secuencia a conjunto
#   No lo genera en orden
#*******************************************************************************

s = set('Hello')
print(s)
s = set((1, 2, 3, 4,5))
print(s)


#*******************************************************************************#   De diccionario a conjunto: conjunto llaves
#*******************************************************************************

d = {1: 'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)
 
s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #    Unión
print(su)

si = s1&s2 #    Unión
print(si)

sr = s1-s2 #    Unión
print(sr)

sp = s2-s1 #    Unión
print(sp)

ss = s1^s2 #    Unión
print(ss)


#*******************************************************************************#   Uso de diccionariios
#*******************************************************************************

capitals= {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
print(capitals)


#*******************************************************************************#   llave:valor
#*******************************************************************************
#   diccionario vacio
d = {}

#   Llave entera, valor string
numNames={1:"One", 2: "Two", 3:"Three"}

#   Llave real, valor string
decNames={1.5:"One and Half", 2.5:"Two and Half", 3.5:"Three and Half"}

# Llave tupla, valor string
items={("Parker","Reynolds","Camlim"):"pen",("LG","Whirlpool","Samsumg"):"Refrigerator"}

# Llave string, valor int
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

#   Reportar llave y valor
for k in capitals:
    print ("Key=" + k + ",Value= " + capitals[k])

#   Nuevo dato para  el diccionario
capitals["México"] = "CDMX"
print(capitals)

#   Borrar dato del diccionario
del capitals["México"] = "CDMX"
print(capitals)

#   Borrar todo el diccionario
del capitals["México"] = "CDMX"
del capitals

#   Reportar llaves
print(romanNums.keys())
 
#   Reportar valores
print(romanNums.values())

#   Juicio de llave (está o no está la llave en el diccionario)
print("I" in rimanNums)
print("X" in rimanNums)
print("XX" not in rimanNums)







