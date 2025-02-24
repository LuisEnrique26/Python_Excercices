
nombre = input('Ingresa tu nombre: ')
materias = int(input('Ingresa el número de materias: '))
calificaciones = []

for calif in range(materias):
    calificacion = float(input(f'Ingresa la calificacion de la materia #{calif + 1}: '))
    calificaciones.append(calificacion)

promdeio = sum(calificaciones) / materias

print(f'{nombre.title()}, el promedio de su cuatrimestre: {promdeio:.2f}')