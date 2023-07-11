### Functions ###

def my_function (): # definición con def y :
    print("Esto es una función")

my_function () # llamamos a "my_function"
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
# def sum_two_values (first_number: int, second_number: int): # no fuerza, puede ignorar, tendríamos que validar dentro
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

# my_result = sum_two_values(1.4, 5.2) # retorna None
my_result = sum_two_values_with_return(10, 5)
print(my_result)
# print (sum_two_values_with_return(10, 5)) # También se podría imprimir directamente

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Moure", name = "Brais") # Podemos hacer que aunque no sigamos el nombre de llamada podamos rectificarlo

# Parámetros por defecto. Si no se indica así daría error porque necesita todos los parámetros
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Para recibir "infinitos" parámetros se usa *
def print_texts(*text):
    print(text)

print_texts("Hola", "Python", "MoureDev")
print_texts("Hola")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")