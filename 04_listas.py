### Listas ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list))

print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # Moure
print(my_other_list[-4]) # 35
# print(my_other_list[4]) # Out of rage IndexError
# print(my_other_list[-5]) # Out of rage IndexError

print(my_list.count(30)) # Cuenta el número de ocurrencias de lo que le pasamos. Ej. El 30 está 2 veces.

# Voy por 3h 29m