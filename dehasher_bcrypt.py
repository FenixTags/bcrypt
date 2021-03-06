from itertools import product
import string
import bcrypt

CHARACTER = string.ascii_lowercase + string.ascii_uppercase + string.digits


def data_input(counter, minLen, maxLen, passHashed):
    passDehashed = None
    print(f"Intento: {counter}", end="")
    for i in range(minLen, maxLen):
        for j in product(CHARACTER, repeat=i):
            word = "".join(j)
            word = word.encode()
            if bcrypt.checkpw(word, passHashed):
                passDehashed = word.decode()
                break
            counter += 1
            for x in range(len(str(counter))):
                print("\b", end="")
            print(f"{counter}", end="")
    return passDehashed


def main():
    minLen = int(input("Ingresa el minimo de caracteres de la contraseña: "))
    maxLen = int(input("Ingresa el maximo de caracteres de la contraseña: "))
    counter = 1

    passHashed = input("Ingrese el hash a crackear: ")
    passHashed = passHashed.encode()
    passDehashed = data_input(counter, minLen, maxLen, passHashed)
    print(f"\nLa contraseña deshasheada es: {passDehashed}")


if __name__ == '__main__':
    main()
