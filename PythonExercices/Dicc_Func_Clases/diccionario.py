# Declarar un diccionario en Python

student = {
    'name': 'Luis',
    'age': 22,
    'language': 'Python',
    'city': 'San José G'
}

# Acceso a valores de un diccionario
print(f'Contenido total del estudiante: {student}')
print(f'Nombre: {student["name"]}')
print(f'Edad: {student.get("age")}')

print('--- Operaciones basicas ---')

# Modificar los valores de un diccionario
student['language'] = 'C++'
print(f'Contenido actual del estudiante una vez modificado el language: {student}')

# Eliminar un elemento de un diccionario
student.pop('city')
print(f'\nContenido del estudiante una vez eliminada la ciudad: {student}')

# Agregar un nuevo elemento
student['food'] = 'Enchiladas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad:  {student}')

print('\n\n\n--- Iterar sobre un diccionario ---')
print('\nIteracion de los elementos de un diccionario, simple ')

for element in student:
    print(f'{element}: {student[element]}')

print('\nIteracion de los elementos de un diccionario, destructuracion - unpaking')

for key, value in student.items():
    print(f'Llave: {key}, Valor: {value}')

print('\n\nIteracion de los elemntos de un diccionario, llaves')

for key in student.keys():
    print(f'Llave: {key}')

print('\n\nIteracion de los elementos de un diccionario, valores')

for value in student.values():
    print(f'Valor: {value}')