###Sets ###
#De base tiene un array

my_set = set()
my_other_set = {} #es la misma que el diccionario

print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) #Aquí ya indica que es un set

print(len(my_other_set))

#print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add("mouredev")
print(my_other_set) #*** Un set no lo ha añadido de forma ordenada, puede hacerlo o no

#Un set no es una estructura ordenada

my_other_set.add("mouredev")
print(my_other_set) 
#*** Un set no admite repetidos ***

#Comprobar que un elemento existe dentro de un set
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

#podemos borrar datos
my_other_set.remove("Moure")
print(my_other_set)

#Vaciar un set
my_other_set.clear()
print(len(my_other_set))

del my_other_set #lo borramos. "del" es propia del sistema
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # CUIDADO!! no tiene por qué coincidir. no concemos el orden que tendrá la lista

my_other_set = {"Kotlin", "Swift", "Python"}

# Juntar 2 sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set)) # no pasa nada porque los elementos son únicos. ".union" no almacena / modifica, devuelve

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # ahora sí añade los últimos (cuidado, no mantiene el orden)

print(my_new_set.difference(my_set)) # muestra los elementos que son diferentes

# revisar el resto de operaciones que se pueden utilizar con los "set"
# Terminado sets
