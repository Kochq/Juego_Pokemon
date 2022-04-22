import random

def probTurno(x, y, pj1, pj2):
    probabilidad = random.randint(0, 100)

    if probabilidad <= x:
        turno = y
        print(f"{pj1.name} ha paralizado a {pj2.name}")
    else:
        turno = abs(y - 1)

    print(probabilidad)
    
    return turno