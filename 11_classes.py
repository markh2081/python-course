### Classes ###

class MyEmptyPerson: # así se define una clase. Se escriben en "camelcase"
    pass # para evitar errores. Si la clase no tuviera nada evitaría que diera error.
    # tiene sentido cuando estamos definiendo clases o funciones

# para instanciar una clase
print(MyEmptyPerson) # también con MyEmptyPerson()

class Person:
    def __init__(self, name, surname): # Constructor de clase, siempre llama a "self". Así podrá recibir parámetros para construir la clase
        self.name = name
        self.surname = surname # ahora sí los almacenamos

my_person = Person("Brais", "Moure")
print(f"{my_person.name} {my_person.surname}")
# 8:26