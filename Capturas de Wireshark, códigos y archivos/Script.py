import sys

def procesar_diccionario(archivo_entrada, archivo_salida):
    contador_contraseñas = 0  
    with open(archivo_entrada, 'r', encoding='latin-1') as f_entrada:
        with open(archivo_salida, 'w', encoding='latin-1') as f_salida:
            for linea in f_entrada:
                palabra = linea.strip()
                if palabra and not palabra[0].isdigit():
                    palabra_modificada = palabra.capitalize() + '0\n'
                    f_salida.write(palabra_modificada)
                    contador_contraseñas += 1
    return contador_contraseñas

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python modificar_diccionario.py <archivo_entrada>")
        sys.exit(1)
    archivo_entrada = sys.argv[1]
    archivo_salida = 'rockyou_mod.dic'
    contador = procesar_diccionario(archivo_entrada, archivo_salida)
    print(f"Diccionario modificado creado: {archivo_salida}")
    print(f"Cantidad de contraseñas en el diccionario modificado: {contador}")

