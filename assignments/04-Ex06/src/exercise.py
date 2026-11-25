# Leer y sumar números de un archivo

def main():
    with open("assignments/04-Ex06/src/numeros.txt", "r") as archivo:
        lineas = archivo.readlines()

        total = 0
        for numero in lineas:
            total += int(numero)

        print(f"Suma total: {total}")

if __name__=='__main__':
    main()
