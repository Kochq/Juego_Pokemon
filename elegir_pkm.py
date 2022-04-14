def elegirPokemonJ1(p1, p2, p3, p4, p5):
    print("\nEscoge a tu Pokemon")
    print(f"""
A - {p1.name}
B - {p2.name}
C - {p3.name}
D - {p4.name}
E - {p5.name}
          """)
    option = input("> ")

    if option.upper() == "A":
        j1 = p1
    elif option.upper() == "B":
        j1 = p2
    elif option.upper() == "C":
        j1 = p3
    elif option.upper() == "D":
        j1 = p4
    elif option.upper() == "E":
        j1 = p5
    else:
        print("Opcion incorrecta")
    
    return j1


def elegirPokemonJ2(p1, p2, p3, p4, p5):
    print("\nEscoge a tu Pokemon")
    print(f"""
A - {p1.name}
B - {p2.name}
C - {p3.name}
D - {p4.name}
E - {p5.name}
          """)
    option = input("> ")

    if option.upper() == "A":
        j2 = p1
    elif option.upper() == "B":
        j2 = p2
    elif option.upper() == "C":
        j2 = p3
    elif option.upper() == "D":
        j2 = p4
    elif option.upper() == "E":
        j2 = p5
    else:
        print("Opcion incorrecta")
    
    return j2
