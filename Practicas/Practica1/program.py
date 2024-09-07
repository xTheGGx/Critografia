import fileinput

# Función para convertir una letra a un número (A = 0, B = 1, ..., Z = 25)
def letra_a_numero(letra):
    return ord(letra.upper()) - ord('A')

# Función para convertir un número a una letra (0 = A, 1 = B, ..., 25 = Z)
def numero_a_letra(numero):
    return chr((numero % 26) + ord('A'))

# Función para multiplicar una matriz 2x2 por un vector 2x1
def multiplicar_matriz_vector(matriz, vector):
    resultado = [0, 0]
    resultado[0] = (matriz[0][0] * vector[0] + matriz[0][1] * vector[1]) % 26
    resultado[1] = (matriz[1][0] * vector[0] + matriz[1][1] * vector[1]) % 26
    return resultado

# Función para encontrar el inverso modular
def mod_inv(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

# Función para encontrar la matriz inversa (mod 26) de una matriz 2x2
def matriz_inversa(matriz):
    det = (matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]) % 26
    det_inv = mod_inv(det, 26)
    
    if det_inv is None:
        return None
    
    # Crear la matriz inversa
    matriz_inv = [
        [(matriz[1][1] * det_inv) % 26, (-matriz[0][1] * det_inv) % 26],
        [(-matriz[1][0] * det_inv) % 26, (matriz[0][0] * det_inv) % 26]
    ]
    return matriz_inv

# Función para cifrar el texto plano usando el cifrado de Hill
def hill_cifrar(texto_plano, matriz_clave):
    # Asegurarse de que el texto plano esté en mayúsculas y sin espacios
    texto_plano = texto_plano.upper().replace(" ", "")
    
    # Si la longitud del texto plano es impar, añadir padding con 'X'
    if len(texto_plano) % 2 != 0:
        texto_plano += 'X'
    
    # Convertir el texto plano a números
    numeros_texto_plano = [letra_a_numero(char) for char in texto_plano]
    
    # Procesar el texto plano en bloques de 2
    texto_cifrado = []
    for i in range(0, len(numeros_texto_plano), 2):
        bloque = numeros_texto_plano[i:i+2]
        resultado = multiplicar_matriz_vector(matriz_clave, bloque)
        texto_cifrado.append(numero_a_letra(resultado[0]))
        texto_cifrado.append(numero_a_letra(resultado[1]))
    
    return ''.join(texto_cifrado)

# Función para descifrar el texto cifrado usando el cifrado de Hill
def hill_descifrar(texto_cifrado, matriz_clave):
    matriz_clave_inversa = matriz_inversa(matriz_clave)
    
    if matriz_clave_inversa is None:
        return "No se puede invertir la matriz"
    
    # Convertir el texto cifrado a números
    numeros_texto_cifrado = [letra_a_numero(char) for char in texto_cifrado]
    
    # Procesar el texto cifrado en bloques de 2
    texto_descifrado = []
    for i in range(0, len(numeros_texto_cifrado), 2):
        bloque = numeros_texto_cifrado[i:i+2]
        resultado = multiplicar_matriz_vector(matriz_clave_inversa, bloque)
        texto_descifrado.append(numero_a_letra(resultado[0]))
        texto_descifrado.append(numero_a_letra(resultado[1]))
    
    return ''.join(texto_descifrado)

# Leer entrada usando fileinput
lineas = []
for linea in fileinput.input():
    lineas.append(linea.strip())

# La primera línea es 'C' para cifrar o 'D' para descifrar
operacion = lineas[0]

# La segunda línea es el texto (texto plano o cifrado)
texto = lineas[1]

# La tercera línea es la clave, que se debe convertir a una matriz 2x2
clave = lineas[2]
letterA = clave[0]
letterB = clave[1]
letterC = clave[2]
letterD = clave[3]
# Convertir la clave a números y formar la matriz clave en el orden correcto (por filas)
matriz_clave = [
    [letra_a_numero(letterA), letra_a_numero(letterC)],  # Primera fila
    [letra_a_numero(letterB), letra_a_numero(letterD)]   # Segunda fila
]


# Si la operación es 'C', realizar el cifrado
if operacion == 'C':
    texto_cifrado = hill_cifrar(texto, matriz_clave)
    print(texto_cifrado)

# Si la operación es 'D', realizar el descifrado
elif operacion == 'D':
    texto_descifrado = hill_descifrar(texto, matriz_clave)
    print(texto_descifrado)
