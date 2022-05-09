import random


def probTurno(x, y):
    probabilidad = random.randint(0, 100)

    if probabilidad <= x:
        turno = y
        print(f"{j1.name} ha paralizado a {j2.name}")
    else:
        turno = abs(y - 1)

    print(probabilidad)

    return turno
