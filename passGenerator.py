from itertools import product
import string


def main():
    minLen = int(input("Ingresa el minimo de caracteres de la contraseña: "))
    maxLen = int(input("Ingresa el maximo de caracteres de la contraseña: "))
    counter = 0
    character = string.ascii_lowercase+string.ascii_uppercase+string.digits

    file_open = open("pass.txt", 'w')

    for i in range(minLen, maxLen):
        for j in product(character, repeat=i):
            word = "".join(j)
            file_open.write(word)
            file_open.write('\n')
            counter += 1
    print(f"La lista de {counter} ha sido creada.")


if __name__ == '__main__':
    main()