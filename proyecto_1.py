import random

# Generar número secreo aleatorio entre 1 y 10.
numero_secreto = random.randint(1,10)

intentos_maximos = 3
intentos = 1

# 'Presentación'
print("Este es un juego para adivinar un número secreto entre 1 y 10.")

# Crear un 'input' para introducir el número.
intento = int(input("Adivina el número secreto. Tienes tres intentos a disposición: "))

# Crear bucle 'while'
while intento != numero_secreto and intentos < intentos_maximos:
    
    if intento < numero_secreto:
        print("Casi. Sube un poco más.")
    elif intento > numero_secreto:
        print("Casi. Pero tienes que bajar más.")

    intentos_restantes = intentos_maximos - intentos

    print(f"¡No has adivinado. Inténtalo otra vez! Te quedan {intentos_restantes} intentos.")

    intento = int(input("Introduce el número secreto: "))
    intentos += 1

if intento == numero_secreto:
    
    print(f"¡Felicidades. Has ganado el juego! El número exacto es {numero_secreto}.") 

else:
    print(f"¡Lo siento. Se acabaron los intentos! El número correcto era {numero_secreto}.")
