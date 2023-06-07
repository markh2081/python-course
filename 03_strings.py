### Strings ###

my_string = "Mi cadena"
my_other_string = 'Mi otra cadena'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # concatenación

my_new_line = "Este es un String \ncon salto de línea" # pueden llevar ciertos caracteres, ej \n -> salto de línea
print(my_new_line)
my_tab_line = "Este es un String \tcon tabulación" # pueden llevar ciertos caracteres, ej \t -> tabulación
print(my_tab_line)
my_scape_line = "\\tEste es un String \\n escapado" # con \ antes del caracter especial (\n, \t, etc)
print(my_scape_line)

# Formateo. Como formatear los strings

name, surname, age = "John", "Doe", 37

print("Mi nombre es {} {} y tengo {}".format(name, surname, age)) # con format -> {}
print("Mi nombre es %s %s y tengo %d" %(name, surname, age)) # con %s, %d, etc.
print("Mi nombre es " + name + " " +  surname + " y tengo " + str(age))
print(f"Mi nombre es {name} {surname} y tengo {age}") # inferencia de datos bien <-- ojo a la "f" del comienzo

# Desempaquetado de variables
language = "Python"
# a, b = language # da error, intenta meter cada caracter en una variable
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # Los caracteres del 1 al 3 empezando desde 0 y el 3o sería el índice 2
print(language_slice)

language_slice = language[1] # Los caracteres del 1 al último empezando desde 0
print(language_slice)

language_slice = language[-2] # Empieza desde el final
print(language_slice)

language_slice = language[0:6:2] # Que me coja todos y después evita los 2os caracteres
print(language_slice)

# Reverse

reversed_language = language[::-1] # Lo mete del final al comienzo
print(reversed_language)

# Funciones

# Si ponemos un punto después de la cadena nos da las distintas opciones
print(language.capitalize()) 
print(language.upper()) 
print(language.count("t")) # Cuenta las T que tiene
print(language.isnumeric()) 
print("1".isnumeric()) 
print(language.lower())
print(language.upper().isupper())
print(language.upper().islower())
print(language.startswith("Py"))
print("Py" == "py") # false
