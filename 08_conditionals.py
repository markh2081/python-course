### Conditionals ###
# Establece flujos de ejecución de nuestro código

my_condition = False

if my_condition: # Si es verdadero se ejecuta. Es lo mismo que poner: if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5
if my_condition == 10: # Revisa que pasa en condition pero no cumple nada y lo da como bueno. Como tiene algo como valor le vale. Esto era en -> if my_condition:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:  # No se ejecuta
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

my_string = ""

if not my_string: # Un string vacío lo da como false (no tiene valor)
    print("Mi cadena de texto está vacía")

if my_string == "Mi cadena de textooooooooooo":
    print("Estas cadenas de texto coinciden")

# ¿Uso de match?
