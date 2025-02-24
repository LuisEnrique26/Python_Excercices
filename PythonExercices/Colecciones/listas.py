from itertools import count

print('manejo de listas \n\n')

my_list= [1,2,3,4,5,6,7,8,9,10,117]
print(f'valores actuales son: {my_list}')
my_list.append(0)
my_list.append(118)
print(f'valores modif de la lista: {my_list}')

#ordenar los elementos de la lista
my_list.sort()

print(f'elementos de la lista prdenados: {my_list}')

my_list[0]='cadena'
my_list.pop()

print(f'valores actuales de la lista EJ:pop: {my_list}')

my_sublist = my_list[0:]
print(f'valores actuales de mi sub lista: {my_sublist}')

print(f'\n\n valores imprimidos de la lista for')
count=0
for item in my_list:
    print(f'elemento de la lista {count}: {item}')
    count += 1