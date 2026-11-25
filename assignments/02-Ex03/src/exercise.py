# Contar palabras en un archivo

def main():
    with open("assignments/02-Ex03/src/texto.txt", "r") as archivo:
        total_palabras = 0

        for linea in archivo:
            total_palabras += len(linea.split())

    print(f"Número de palabras: {total_palabras}")

if __name__=='__main__':
    main()
