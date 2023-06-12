### Listas ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list))

print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # Moure
print(my_other_list[-4]) # 35
# print(my_other_list[4]) # Out of rage IndexError
# print(my_other_list[-5]) # Out of rage IndexError

print(my_list.count(30)) # Cuenta el número de ocurrencias de lo que le pasamos. Ej. El 30 está 2 veces.

# Voy por 3h 29m

# se pueden inicializar variables en base a una lista manteniendo el orden (no tiene que ver co el nombre de la variable)
age, height, name, surname = my_other_list
print(name)
# age, height, name = my_other_list # daría error, necesita todos los elementos (4)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# se pueden concatenar dos listas en el orden en el que están
print(my_list + my_other_list)

# dan error
# print(my_list - my_other_list)
# print(my_list * my_other_list)

##########
# Una lista es mutable
##########
# Se pueden añadir elementos
# my_other_list.append añade al final
my_other_list.append("Empresa")
print(my_other_list)

# my_otherList.insert -> dime el índice donde quieres que lo inserte y lo que quieres insertar
my_other_list.insert(1, "Rojo") # color favorito
print(my_other_list)

# también se puede sobre escribir lo que hay en un índice
my_other_list[1] = "Azul"
print(my_other_list)

# también podemos eliminar
# my_other_list.remove. Puedes decirle qué quieres eliminar (tenemos que conocerlo). Si le pasas un "índice" o no existe, DA ERROR
my_other_list.remove("Azul")
print(my_other_list)
# solo elimina el primer elemento en caso de repetirse
my_list.remove(30) # hay 2
print(my_list)

# my_list.pop() elimina el último elemento por defecto, y devuelve el elemento que hemos "desapilado". Si no tiene elementos DA ERROR
print(my_list.pop())
print(my_list)
# le indicamos el índice del elemento que quiero eliminar

# si queremos guardarlo tenemos que asignarlo a una variable
my_pop_element = my_list.pop(2)
print(my_pop_element)

# Podemos copiar una lista
my_new_list = my_list.copy() # devuelve una copia de los valores de la lista

# borrar el elemento que está en un índice, sin que me lo devuelva
del my_list[2] # en este momento my_list en el índice 2 tiene el número 52
print(my_list)
# *** "del" es del sistema, borra la variable / elemento

# borrar la lista entera
my_list.clear()
print(my_list)
print(my_new_list) # se ve que es una copia en el punto donde se copio

# dar una vuelta a la lista. no devuelve el valor al reves, da la vuelta a la lista en si
my_new_list.reverse()
print(my_new_list)

# my_new_list.sort ordenar una lista. Se le pueden indicar criterios (también con el [-1])
'''
--
(*, key: None = None, reverse: bool = False) -> None
--
(*, key: (int) -> SupportsRichComparison, reverse: bool = False) -> None
--
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.
'''
my_new_list.sort()
print(my_new_list)

# Sublistas
print(my_new_list[1:2]) # entre el elemento 1 y 2 tenemos el 30 # [24, 30, 35, 52]




# tipos dinámicos
my_list = "Hola Python" # deja de ser una lista
print(my_list)
print(type(my_list))


# CONSTANTES. En Python no se pueden crear constantes, lo que se "suele hacer" es indicar que es una constante (para que no lo modifiquen)
# poniendo el nombre de la variable en mayúsculas, aunque puede haber variables finales... (se verá más adelante)
