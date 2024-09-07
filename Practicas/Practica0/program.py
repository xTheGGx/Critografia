import fileinput

suma = 0

# Leer todos los números de la entrada usando fileinput
for line in fileinput.input():
    numero = float(line.strip())
    suma += numero

# Imprimir el resultado de la suma
print(int(suma))
