### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
# Se puede poner un else al if cuando sale del bucle
# elif my_condition == 10: # No acepta "elif"
else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la ejecución. Mi condición es 15")
        # Para salir de golpe de un bucle
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: # Se va a repetir tantas veces como elementos tenga la lista
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for element in my_dict: # Imprime las keys, NO imprime los values
    print(element)
# for element in my_dict.values():

for element in my_dict:
    print(element)
else: # también tenemos "else"
    print("El bucle for para mi diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado") # No se imprime porque ha salido con break

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # otra palabra reservada que se puede utilizar
    print("Se ejecuta") # No se pintaría "Se ejecuta" después de "Edad", continua volviendo al for
else:
    print("El bucle for para mi diccionario ha finalizado") # No se imprime porque ha salido con break

print("La ejecución continúa")