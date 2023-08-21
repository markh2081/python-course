### Classes ###

class MyEmptyPerson: # así se define una clase. Se escriben en "camelcase"
    pass # para evitar errores. Si la clase no tuviera nada evitaría que diera error.
    # tiene sentido cuando estamos definiendo clases o funciones

# para instanciar una clase
print(MyEmptyPerson) # también con MyEmptyPerson()
print("----------------------")

class Person01:
    def __init__(self, name, surname): # Constructor de clase, siempre llama a "self". Así podrá recibir parámetros para construir la clase
        self.name = name
        self.surname = surname # ahora sí los almacenamos

my_person01 = Person01("Brais", "Moure")
print(f"{my_person01.name} {my_person01.surname}")
print("----------------------")

class Person02:
    def __init__(self, name, surname): # Constructor de clase, siempre llama a "self". Así podrá recibir parámetros para construir la clase
        self.full_name = f"{name} {surname}"

my_person02 = Person02("Brails", "Moure")
print(my_person02.full_name)
print("----------------------")

# podemos añadirle funciones
class Person03:
    def __init__(self, name, surname): # Constructor de clase, siempre llama a "self". Así podrá recibir parámetros para construir la clase
        self.full_name = f"{name} {surname}"

    def walk(self): 
        # hay que pasarle self para poder utilizar sus properties
        # la forma de llamar a la misma clase es "self"
        print(f"{self.full_name} está caminando")

my_person03 = Person03("Brails", "Moure")
print(my_person03.full_name)
my_person03.walk()
print("-------------------------")

class Person04:
    def __init__(self, name, surname, alias = "Sin alias"): # le damos un valor por defecto a "alias"
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self): 
        # hay que pasarle self para poder utilizar sus properties
        # la forma de llamar a la misma clase es "self"
        print(f"{self.full_name} está caminando")

my_person04 = Person04("Brails", "Moure")
print(my_person04.full_name)
my_person04.walk()

my_other_person04 = Person04("Brails", "Moure", "MoureDev")
my_other_person04.walk()
# Podemos acceder a las propiedades del objeto
my_other_person04.full_name = "Héctor de León (El loco de los perros)"
# En este caso se lo hemos cambiado
print(my_other_person04.full_name)

# Le podemos cambiar el tipo
my_other_person04.full_name = 8796
print(my_other_person04.full_name)
print("-------------------------")

# Como hacer que tenga propiedades privadas
class Person05:
    def __init__(self, name, surname, alias = "Sin alias"): # le damos un valor por defecto a "alias"
        self.full_name = f"{name} {surname} ({alias})" # propiedad pública
        # Se hace con dos guiones bajos delante
        self.__name = name  # Propiedad privada

    # para poder acceder a la propiedad necesitaríamos un getter (o un setter)
    def get_name(self):
        return self.__name

my_person05 = Person05("Brails", "Moure")
# print(my_person05.__name) # da error, no podemos acceder a una propiedad privada

print(my_person05.get_name())