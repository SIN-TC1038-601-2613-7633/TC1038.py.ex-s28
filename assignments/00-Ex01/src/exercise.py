# Crear un archivo de texto

def main():
    texto = input("Ingrese un texto:")

    with open("assignments/00-Ex01/src/texto.txt", "w") as archivo:
        archivo.write(texto)

if __name__=='__main__':
    main()
