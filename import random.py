import random
import time
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

caras = [
    """
    -------
    |     |
    |  •  |
    |     |
    -------
    """,
    """
    -------
    | •   |
    |     |
    |   • |
    -------
    """,
    """
    -------
    | •   |
    |  •  |
    |   • |
    -------
    """,
    """
    -------
    | • • |
    |     |
    | • • |
    -------
    """,
    """
    -------
    | • • |
    |  •  |
    | • • |
    -------
    """,
    """
    -------
    | • • |
    | • • |
    | • • |
    -------
    """
]

print("🎲 Simulador de Dados 3000 🎲")
input("Presiona ENTER para lanzar los dados...")

for i in range(5):
    limpiar()
    print("Lanzando..." + "🎲" * (i+1))
    time.sleep(0.3)

limpiar()
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Tu tirada es:")
print(caras[dado1 - 1])
print(caras[dado2 - 1])
print(f"🎯 Total: {dado1 + dado2}\n")

if dado1 == dado2:
    print("¡Wow! 🎉 ¡Doble! Tienes suerte hoy 😎")
else:
    print("Nada mal 😁 ¡Intenta otra vez!")

print("Actualización - Prueba Commit 10:40pm")