### Tuples ###

# como definir una tupla
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

#no se ven operaciones de inserción...
print(my_tuple.count("Brais")) # cuenta las veces que hay el elemento que le hemos pasado
print(my_tuple.count("Empresa"))
# .index devuelve el índice que ocupa el valor que le hemos pasado (la primera ocurrencia). También existe en las listas
print(my_tuple.index("Moure")) 

'''
# LAS TUPLAS NO TE DEJA CAMBIARLAS, SON VALORES INMUTABLES. No deja modificar ni añadir / borrar
my_tuple[1] = 1.80 # error: TypeError: 'tuple' object does not support item assignment
print(my_tuple)
'''

# se pueden sumar
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) 

print(my_sum_tuple[3:6]) # slice Moure, Brais, 35

# Convertir tupla en lista
my_tuple = list(my_tuple) 
print(type(my_tuple))

my_tuple[4] = "Empresa"
my_tuple.insert(1, "Azul")
print(my_tuple)

# lo vuelvo a setear como tupla
my_tuple = tuple(my_tuple)
print(type(my_tuple))

#del my_tuple [2] #TypeError: 'tuple' object doesn't support item deletion
del my_tuple # la borra. Es un poco incoherente ya que la modifica
#print(my_tuple) NameError: name 'my_tuple' is not defined
# *** "del" es del sistema, borra la variable / elemento

