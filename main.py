# Abrimos el archivo para leerlo
with open('input', 'r') as archivo:
  # Leemos todas las líneas del archivo
  lineas = archivo.readlines()

# Guardamos los valores en variables
numero1 = int(lineas[0].strip())  # Primera línea
numero2 = int(lineas[1].strip())  # Segunda línea

output = numero1 + numero2  # Sumamos los valores	

# Mostramos los valores para verificar
print(output)

