gencode = {}

with open ('gencode.txt', 'r') as geneticcode:
    for line in geneticcode:
        cod = line [:3]
        ami = line [8:9]
        gencode [cod] = ami
