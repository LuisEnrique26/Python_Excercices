print('ejecuten con tuplas\n\n')

tupla_informacion = ('bejamin Carmine', 18,80.4)
print(f'informa de la tupla: {tupla_informacion}')

full_name, age, salary = tupla_informacion
print(f'name: {full_name}, Age: {age}, Salary: {salary}')
print('\n\n impresion de la tupla')

for item in tupla_informacion:
    print(item)
    