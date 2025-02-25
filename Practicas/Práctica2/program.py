def KSA(key):
    """Key-Scheduling Algorithm (KSA)"""
    S = list(range(256))  # Inicializa el array S con valores de 0 a 255
    j = 0
    keylength = len(key)
    
    # Permutación inicial de S usando la clave
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # Intercambiar S[i] y S[j]
    
    return S

def PRGA(S, n):
    """Pseudo-random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    keystream = []
    
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Intercambiar S[i] y S[j]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    
    return keystream

def rc4(key, plaintext):
    """RC4 cifrado y descifrado"""
    # Convertir clave y texto plano a bytes
    key = [ord(c) for c in key]
    plaintext = [ord(c) for c in plaintext]
    
    # KSA: Inicializar S con la clave
    S = KSA(key)
    
    # PRGA: Generar keystream del mismo tamaño que el texto plano
    keystream = PRGA(S, len(plaintext))
    
    # XOR entre keystream y el texto plano para obtener el cifrado
    ciphertext = [p ^ k for p, k in zip(plaintext, keystream)]
    
    # Convertir el resultado a formato hexadecimal
    return ''.join([format(c, '02X') for c in ciphertext])

def main():
    # Leer la entrada
    key = input().strip()
    plaintext = input().strip()
    
    # Ejecutar el cifrado RC4
    ciphertext = rc4(key, plaintext)
    
    # Mostrar el resultado en formato hexadecimal
    print(ciphertext)

if __name__ == "__main__":
    main()
