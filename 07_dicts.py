### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
# Tenemos una relación clave valor. Tenemos una estructura para relacionar datos, podemos guardar datos por clave valor
print(my_other_dict)

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Puede tener otro tipo de datos
    1: 1.77
    }
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
# Cuenta el número de claves

print(my_dict["Nombre"]) # Así podemos acceder directamente a una de las propiedades / elementos del dict

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Al igual que podemos acceder para leer podemos acceder para sobre-escribir

print(my_dict[1])

my_dict["Calle"] = "Calle MoureDev"
print(my_dict) # Se pueden agregar nuevos campos

del my_dict["Calle"] # Borramos el elemento "Calle"
print(my_dict)

print("Moure" in my_dict)
print("Apellido" in my_dict) # Donde busca es en las propiedades

print(my_dict.items()) # Devuelve un listado de cada uno de los items
print(my_dict.keys()) # Devuelve las claves
print(my_dict.values()) # Devuelve solo los valores que contienen las "keys"
# print(my_dict.fromkeys()) # Devuelve un diccionario de las keys que le pasemos
print(my_dict.fromkeys(("Nombre", 1))) # Lo crea pero solo con las keys, sin valores dentro

my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict) #ha creado un diccionario sin valores
# Si le pasamos una key que no exista dentro del diccionario nos lo crea / añade igual. Realmente no hace nada.
# Sería lo mismo que llamar a dict (es palabra reservada) .fromkeys -> dict.fromkeys(("Nombre", 1, "Piso"))

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Puede recibir una lista
print(my_new_dict)

my_list = ("Nombre", 1, "Piso")
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)


my_new_dict = dict.fromkeys(my_dict) # Puede recibir otro diccionario (lo crea vacío)
print(my_new_dict)


my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure")) # Como segundo parámetro puede recibir valores para que tenga dentro.
# *** Es el valor por defecto para TODOS los elementos ***
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict)
# Es un valor que recibe y que se va a duplicar en todas las claves

my_values = my_new_dict.values()
print(type(my_values)) # es un diccionario de valores (dict_values)
# Si queremos una lista tenemos que transformarlo (list(my_new_dict.values()))


print(list(my_new_dict)) # Crea una lista con las claves
print(tuple(my_new_dict))
print(set(my_new_dict))

