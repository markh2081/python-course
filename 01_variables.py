# Variables
# convenciones - minúsculas, snake_case, etc. si quieres usar palabra reservada, que comience por "_"

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # str es una built-in function
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concateniación de variables en un print
# print puede llevar diferentes argumentos separados por ,
print(my_string_variable, my_int_variable, my_bool_variable) # My String variable 5 False
# print(my_string_variable, str(my_int_variable), my_bool_variable)

print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) # Abrv length - longitud string
print("Longitud de my_string_variable:", len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintas!
name, surname, alias, age = "Marcos", "Rivera", 'markh', 45
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)
# puede tener sentido para funciones que devuelven dos valores

# Inputs

# Una variable puede mutar su valor
"""
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)
"""

# Cambiamos su tipo
name = 45
age = 'Marcos'
print(name)
print(age)

