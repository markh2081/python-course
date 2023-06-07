### Operadores ###

# = += -= *= /= %= //= **= &= |= ^= >>= <<=
# + - * / % ...

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # módulo -> resto que tenemos
print(10 // 3) # Flor-division. Acaba aproximada a un número entero
print(2 ** 3) # Exponente. 2 elevado a 3
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola " + "Python " + "¿Que tal?") # Concatena cadenas
# print("Hola" + 5) # error
print("Hola " * 5) # Aparece 4 veces
print("Hola " + str(5)) # convirtiendo sí

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

print("aaaa" >= "abaa") # no valida la cantidad de caracteres, valda ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # así sí compara longitud
print("AAAA" >= "aaaa") # tiene en cuenta mayúsculas

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python") # Lógica booleana. False y False es False, True y False es False, True y True es True
print(3 > 4 or "Hola" > "Python") # False y False es False, True y False es True
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 > 4))

# Voy por 2h 17m

