def habilidades(jugador):
    if jugador.name == "Pikachu":
        while True:
            print("""Elegir habilidad:
A - Onda Trueno
B - Impactrueno
C - Electro Bola
D - Rayo
              """)
            opcion = input("> ")
            if opcion.upper() == "A":
                ataque = 15
                break
            elif opcion.upper() == "B":
                ataque = 20
                break
            elif opcion.upper() == "C":
                ataque = 18
                break
            elif opcion.upper() == "D":
                ataque = 16
                break
            else:
                print("Opcion Invalida")

    elif jugador.name == "Charmander":
        while True:
            print("""Elegir habilidad:
A - Anillo Igneo
B - Ascuas
C - Lanzallamas
D - Infierno
              """)
            opcion = input("> ")
            if opcion.upper() == "A":
                ataque = 15
                break
            elif opcion.upper() == "B":
                ataque = 20
                break
            elif opcion.upper() == "C":
                ataque = 18
                break
            elif opcion.upper() == "D":
                ataque = 16
                break
            else:
                print("Opcion Invalida")

    elif jugador.name == "Bulbasaur":
        while True:
            print("""Elegir habilidad:
A - Drenadoras
B - Latigo Cepa
C - Hoja afilada
D - Rayo Solar
              """)
            opcion = input("> ")
            if opcion.upper() == "A":
                ataque = 15
                break
            elif opcion.upper() == "B":
                ataque = 20
                break
            elif opcion.upper() == "C":
                ataque = 18
                break
            elif opcion.upper() == "D":
                ataque = 16
                break
            else:
                print("Opcion Invalida")

    elif jugador.name == "Squirtle":
        while True:
            print("""Elegir habilidad:
A - Surf
B - Pistola Agua
C - Hidropulso
D - Hidrobomba
              """)
            opcion = input("> ")
            if opcion.upper() == "A":
                ataque = 15
                break
            elif opcion.upper() == "B":
                ataque = 20
                break
            elif opcion.upper() == "C":
                ataque = 18
                break
            elif opcion.upper() == "D":
                ataque = 16
                break
            else:
                print("Opcion Invalida")

    elif jugador.name == "La Tota":
        while True:
            print("""Elegir habilidad:
A - Rayo Infinito
B - Terremoto
C - Surf
D - Anillo Igneo
              """)
            opcion = input("> ")
            if opcion.upper() == "A":
                ataque = 16
                break
            elif opcion.upper() == "B":
                ataque = 21
                break
            elif opcion.upper() == "C":
                ataque = 19
                break
            elif opcion.upper() == "D":
                ataque = 17
                break
            else:
                print("Opcion Invalida")

    return ataque
