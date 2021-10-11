# ------------------------------------------------------------
# Clase 140
# Encriptamiento
# pip install bcrypt
# ------------------------------------------------------------

# Importamos la libreria bcrypt
import bcrypt_encrypt

# Texto plano
textoPlano = "password"
print("Texto plano: ", textoPlano)
input()

# Debemos tenerla como bytes
textoPlano = textoPlano.encode()
print("Texto plano en bytes: ", textoPlano)
input()

# Generamos semilla
semilla = bcrypt_encrypt.gensalt()
print("Semilla: ", semilla)
print("Semilla Type: ", type(semilla))
input()

# Hasheamos el texto
textHash = bcrypt_encrypt.hashpw(textoPlano, semilla)
print("Texto hash: ", textHash)
input()

# Ahora vamos a comprobarla, recuerda que pass_hasheada puede prevenir que tu base de datos
print("Comprobando contraseñas...")
print("Texto Plano: ", textoPlano)
print("Texto Hash: ", textHash)

# Verificamos si coinciden con el metodo checkpw
if bcrypt_encrypt.checkpw(textoPlano, textHash):
    print("Ok, las contraseñas coinciden")
else:
    print("Contraseña incorrecta")
