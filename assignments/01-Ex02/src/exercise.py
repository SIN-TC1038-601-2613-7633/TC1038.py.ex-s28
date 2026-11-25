# Leer un archivo y contar lineas

def main():
    with open("assignments/01-Ex02/src/datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"Número de líneas: {len(lineas)}")

if __name__=='__main__':
    main()
