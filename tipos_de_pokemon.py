def tipos(jugador1, jugador2):
    if jugador1.tipo == "Electrico" and jugador2.tipo == "Agua":
        efectivo = 2
    elif jugador1.tipo == "Electrico" and jugador2.tipo == "Planta":
        efectivo = 0.5
    elif jugador1.tipo == "Electrico" and jugador2.tipo == "Fuego":
        efectivo = 1
    elif jugador1.tipo == "Electrico" and jugador2.tipo == "Dragon":
        efectivo = 0.5
    elif jugador1.tipo == "Agua" and jugador2.tipo == "Electrico":
        efectivo = 1
    elif jugador1.tipo == "Agua" and jugador2.tipo == "Planta":
        efectivo = 0.5
    elif jugador1.tipo == "Agua" and jugador2.tipo == "Fuego":
        efectivo = 2
    elif jugador1.tipo == "Agua" and jugador2.tipo == "Dragon":
        efectivo = 0.5
    elif jugador1.tipo == "Planta" and jugador2.tipo == "Electrico":
        efectivo = 1
    elif jugador1.tipo == "Planta" and jugador2.tipo == "Agua":
        efectivo = 2
    elif jugador1.tipo == "Planta" and jugador2.tipo == "Fuego":
        efectivo = 0.5
    elif jugador1.tipo == "Planta" and jugador2.tipo == "Dragon":
        efectivo = 0.5
    elif jugador1.tipo == "Fuego" and jugador2.tipo == "Electrico":
        efectivo = 1
    elif jugador1.tipo == "Fuego" and jugador2.tipo == "Planta":
        efectivo = 2
    elif jugador1.tipo == "Fuego" and jugador2.tipo == "Agua":
        efectivo = 0.5
    elif jugador1.tipo == "Fuego" and jugador2.tipo == "Dragon":
        efectivo = 0.5
    elif jugador1.tipo == "Dragon" and jugador2.tipo == "Electrico":
        efectivo = 1
    elif jugador1.tipo == "Dragon" and jugador2.tipo == "Planta":
        efectivo = 1
    elif jugador1.tipo == "Dragon" and jugador2.tipo == "Fuego":
        efectivo = 1
    elif jugador1.tipo == "Dragon" and jugador2.tipo == "Agua":
        efectivo = 1
    
    return efectivo
