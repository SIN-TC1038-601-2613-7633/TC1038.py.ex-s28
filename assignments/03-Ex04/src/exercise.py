# Contar palabras en un archivo

def main():

    palabra_a_buscar = input("Ingrese una palabra:")

    with open("assignments/03-Ex04/src/documento.txt", "r") as archivo:

        tot_palabras = 0

        for linea in archivo:
            palabras = linea.split()

            for palabra in palabras:
                if palabra_a_buscar in palabra:
                    tot_palabras +=1

        print(f"Núnmero de ocurrencias: {tot_palabras}")


if __name__=='__main__':
    main()