from random import randint
import sys


def inicializar_laberinto(laberinto, dimension):
    for i in range(dimension):
        laberinto.append([])
        for j in range(dimension):
            laberinto[i].append(randint(0, 10000) % 2)


def imprimir_laberinto(laberinto):
    for i in range(len(laberinto)):
        print laberinto[i]


def imprimirLaberinto(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto)):
            if laberinto[i][j] == -1:
                sys.stdout.write(str(5) + " ")
            else:
                sys.stdout.write(str(laberinto[i][j]) + " ")
        print ""


def cargar_laberinto():
    #laberinto = []
    try:
        with open('laberinto', 'r') as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(0, 0)
            print(size)
            #for i in range(size):
            #    laberinto.append([])
            #    c = f.read(1)
            #    while c != '\n':
            #        laberinto[i].append(c)
            #        c = f.read(1)
            #print laberinto
    except IOError:
        print('El archivo no existe')


def preparar_laberinto(laberinto):
    for i in range(len(laberinto)):
        for j in range(len(laberinto)):
            if laberinto[i][j] == 1:
                laberinto[i][j] = -1
    for i in range(len(laberinto)):
        for j in range(len(laberinto)):
            if laberinto[i][j] != -1:
                if i > 0:
                    if laberinto[i - 1][j] != -1:
                        laberinto[i][j] = laberinto[i][j] + 1
                if j > 0:
                    if laberinto[i][j - 1] != -1:
                        laberinto[i][j] = laberinto[i][j] + 1
                if i < len(laberinto) - 1:
                    if laberinto[i + 1][j] != -1:
                        laberinto[i][j] = laberinto[i][j] + 1
                if j < len(laberinto) - 1:
                    if laberinto[i][j + 1] != -1:
                        laberinto[i][j] = laberinto[i][j] + 1


def evaluar_derecha(laberinto, direccion, posicion, mayor):
    if posicion[1] < len(laberinto) - 1 and\
    laberinto[posicion[0]][posicion[1] + 1] > mayor[1]:
        mayor[0] = 0
        mayor[1] = laberinto[posicion[0]][posicion[1] + 1]


def evaluar_abajo(laberinto, direccion, posicion, mayor):
    if posicion[0] < len(laberinto) - 1 and\
    laberinto[posicion[0] + 1][posicion[1]] > mayor[1]:
        mayor[0] = 1
        mayor[1] = laberinto[posicion[0] + 1][posicion[1]]


def evaluar_izquierda(laberinto, direccion, posicion, mayor):
    if posicion[1] > 0 and\
    laberinto[posicion[0]][posicion[1] - 1] > mayor[1]:
        mayor[0] = 2
        mayor[1] = laberinto[posicion[0]][posicion[1] - 1]


def evaluar_arriba(laberinto, direccion, posicion, mayor):
    if posicion[0] > 0 and\
    laberinto[posicion[0] - 1][posicion[1]] > mayor[1]:
        mayor[0] = 3
        mayor[1] = laberinto[posicion[0] - 1][posicion[1]]


def tiene_solucion(laberinto, posicion=[0, 0]):
    direccion = 0
    if laberinto[posicion[0]][posicion[1]] != -1:
        while direccion != -1 and (posicion[0] != len(laberinto) - 1 or\
        posicion[1] != len(laberinto) - 1):
            direccion = puedo_avanzar(laberinto, direccion, posicion)
            if direccion != -1:
                avanza(laberinto, direccion, posicion)
    if posicion[0] == len(laberinto) - 1\
    and posicion[1] == len(laberinto) - 1:
        return True
    else:
        return False


def puedo_avanzar(laberinto, direccion, posicion):
        direccion = buscar_mayor(laberinto, direccion, posicion)
        if not camino_posible(laberinto, direccion, posicion):
            return -1
        return direccion


def buscar_mayor(laberinto, direccion, posicion):
    mayor = [direccion, -1]
    if mayor[0] == 0:
        evaluar_derecha(laberinto, direccion, posicion, mayor)
        evaluar_abajo(laberinto, direccion, posicion, mayor)
        evaluar_arriba(laberinto, direccion, posicion, mayor)
        evaluar_izquierda(laberinto, direccion, posicion, mayor)
    elif mayor[0] == 1:
        evaluar_derecha(laberinto, direccion, posicion, mayor)
        evaluar_abajo(laberinto, direccion, posicion, mayor)
        evaluar_izquierda(laberinto, direccion, posicion, mayor)
        evaluar_arriba(laberinto, direccion, posicion, mayor)
    elif mayor[0] == 2:
        evaluar_abajo(laberinto, direccion, posicion, mayor)
        evaluar_arriba(laberinto, direccion, posicion, mayor)
        evaluar_izquierda(laberinto, direccion, posicion, mayor)
        evaluar_derecha(laberinto, direccion, posicion, mayor)
    elif mayor[0] == 3:
        evaluar_derecha(laberinto, direccion, posicion, mayor)
        evaluar_arriba(laberinto, direccion, posicion, mayor)
        evaluar_izquierda(laberinto, direccion, posicion, mayor)
        evaluar_abajo(laberinto, direccion, posicion, mayor)
    return mayor[0]


def camino_posible(laberinto, direccion, posicion):
    comprobacion = True
    if direccion == 0:
        if laberinto[posicion[0]][posicion[1] + 1] == 0 or\
        laberinto[posicion[0]][posicion[1] + 1] == -1:
            comprobacion = False
    elif direccion == 1:
        if laberinto[posicion[0] + 1][posicion[1]] == 0 or\
        laberinto[posicion[0] + 1][posicion[1]] == -1:
            comprobacion = False
    elif direccion == 2:
        if laberinto[posicion[0]][posicion[1] - 1] == 0 or\
        laberinto[posicion[0]][posicion[1] - 1] == -1:
            comprobacion = False
    elif direccion == 3:
        if laberinto[posicion[0] - 1][posicion[1]] == 0 or\
        laberinto[posicion[0] - 1][posicion[1]] == -1:
            comprobacion = False
    return comprobacion


def avanza(laberinto, direccion, posicion):
    laberinto[posicion[0]][posicion[1]] =\
    laberinto[posicion[0]][posicion[1]] - 1
    if direccion == 0:
        posicion[1] = posicion[1] + 1
    elif direccion == 1:
        posicion[0] = posicion[0] + 1
    elif direccion == 2:
        posicion[1] = posicion[1] - 1
    elif direccion == 3:
        posicion[0] = posicion[0] - 1


def guardando_resupesta(respuesta):
    try:
        f = open('respuesta.txt', 'w')
        if respuesta:
            f.write('El laberinto tiene solucion')
        else:
            f.write('El laberinto no tiene solucion')
        f.close()
    except:
        print("No se pudo abrir el archivo respuesta.txt")


def main():
    #cargar_laberinto()
    #laberinto = []
    #inicializar_laberinto(laberinto, 5)
    #imprimir_laberinto(laberinto)
    #preparar_laberinto(laberinto)
    #guardando_resupesta(tiene_solucion(laberinto))


if __name__ == "__main__":
    main()
