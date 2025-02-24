try:
    pat = '/home/luisenriquepg/Documentos/archivo.txt'
    new_file = open(pat, 'r')
    data = new_file.readlines()
    #print(data)
    #one_line = new_file.readline()
    #print(one_line)

    for line in data:
        print(line)

    #new_files = open('/home/luisenriquepg/Documentos/archivo.txt', 'w')
    #new_files.write("Hello World\n")
    #new_files.write("Hello\n")
    #new_files.write("World\n")
    #new_files.close()
except Exception as e:
    print(e)