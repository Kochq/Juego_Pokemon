import random
from tipos_de_pokemon import tipos
from habilidades import habilidades
from elegir_pkm import elegirPokemonJ1, elegirPokemonJ2 
from ganadores import win

class Pokemon:
    def __init__(self, name, ataque, vida, tipo):
        self.name = name
        self.ataque = ataque
        self.vida = vida
        self.tipo = tipo


p1 = Pokemon("Pikachu", 15, 100, "Electrico")
p2 = Pokemon("Charmander", 15, 100, "Fuego")
p3 = Pokemon("Bulbasaur", 15, 100, "Planta")
p4 = Pokemon("Squirtle", 15, 100,"Agua")
p5 = Pokemon("La Tota", 15, 100, "Dragon")


def juego():
    while True:
        j1 = elegirPokemonJ1(p1, p2, p3, p4, p5) 
        j2 = elegirPokemonJ2(p1, p2, p3, p4, p5) 
        turno = random.randint(0,1)
        while j1 == j2:
            j1 = elegirPokemonJ1(p1, p2, p3, p4, p5) 
            j2 = elegirPokemonJ2(p1, p2, p3, p4, p5) 
            print("Opcion invalida")
        while j1.vida > 0 and j2.vida > 0:
            if turno == 1:
                print("="*73)
                print(f"Es el turno de {j1.name}")
                ataque = habilidades(j1)
                ataque *= tipos(j1, j2)
                j1.ataque = ataque
                j2.vida -= j1.ataque
                print(f"{j1.name} le ha hecho {j1.ataque} puntos de daño a {j2.name}")
                print(f"{j1.name}: {j1.vida}HP")
                print(f"{j2.name}: {j2.vida}HP")
                turno = 0
            else:
                print("="*73)
                print(f"Es el turno de {j2.name}")
                ataque = habilidades(j2)
                ataque *= tipos(j2, j1)
                j2.ataque = ataque
                j1.vida -= j2.ataque
                print(f"{j2.name} le ha hecho {j2.ataque} puntos de daño a {j1.name}")
                print(f"{j1.name}: {j1.vida}HP")
                print(f"{j2.name}: {j2.vida}HP")
                turno = 1

        if j1.vida <= 0:
            win(j2)
        else:
            win(j1)

        print("Quieres volver a jugar? [S/n]")
        opcion = input("> ")
        if opcion.upper() == "S":
            j1.vida = 100
            j2.vida = 100
            continue
        else:
            exit()


juego()
