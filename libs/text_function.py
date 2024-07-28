def txt_reader(file_name):
    file = open(file_name,'r')
    for line in file:
        print(line,end='')
    file.close()