from itertools import product
import string
import bcrypt


def main():
    minLen = int(input("Ingresa el minimo de caracteres de la contraseña: "))
    maxLen = int(input("Ingresa el maximo de caracteres de la contraseña: "))
    counter = 0
    character = string.ascii_lowercase+string.ascii_uppercase+string.digits

    passHashed = input("Ingrese el hash a crackear: ")
    passHashed = passHashed.encode()
    passDehashed = None

    for i in range(minLen, maxLen):
        for j in product(character, repeat=i):
            word = "".join(j)
            word = word.encode()
            if bcrypt.checkpw(word, passHashed):
                passDehashed = word.decode()
                break
            counter += 1
    print(f"La contraseña deshasheada es: {passDehashed}")


if __name__ == '__main__':
    main()
