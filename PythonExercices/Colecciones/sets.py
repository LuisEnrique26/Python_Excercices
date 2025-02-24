from traceback import print_tb

print('ejemplo de set')

first_collection={1,2,3,4,5,6,7}
second_collection={8,9,10,11,12,13,}

print(f'mi collectio tipo set: {type(first_collection)}')

first_collection.add(6)
print(f'mi collection actualizada: {set(first_collection)}')

first_collection.add('hola')
print(f'mi collection actualizada, ADD {set(first_collection)}')

print('\n\nprint de la seg collection \n')
for item in first_collection:
    print(item)

    union_set = first_collection.union(second_collection)
    intersection_set = first_collection.intersection(second_collection)
    diference_set = first_collection.difference(second_collection)

    print(f'union de las collection {union_set}')
    print(f'intersection de las collection {intersection_set}')
    print(f'diferencia de la collection {diference_set}')
