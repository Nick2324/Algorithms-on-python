matriz_de_caminos = []


def inicializar_caminos(numero_caminos):
#    for i in range(numero_caminos):
#        matriz_de_caminos.append([])
#        for j in range(numero_caminos):
#            matriz_de_caminos[i].append(0)
    matriz_de_caminos = [[0 for i in range(numero_caminos)]\
     for i in range(numero_caminos)]
     print matriz_de_caminos


def adicionar_origen_destino(numero_od=1):
    lista_adicion = []
    for i in range(numero_od):
        lista_adicion.append([])
    for i in range(numero_od):
        for j in range(len(matriz_de_caminos) + numero_od):
            lista_adicion[i].append(0)
    for i in range(len(matriz_de_caminos)):
        for j in range(numero_od):
            matriz_de_caminos[i].append(0)
    matriz_de_caminos.extend(lista_adicion)


def eliminar_origen_destino(origen):
    matriz_de_caminos[origen].pop()
    matriz_de_caminos.remove(matriz_de_caminos[origen])


def adicionar_camino(origen, destino):
    matriz_de_caminos[origen][destino] = 1


def eliminar_camino(origen, destino):
    matriz_de_caminos[origen][destino] = 0


def numero_caminos_origen(origen):
    return matriz_de_caminos[i].count(1)


def numero_caminos_destino(destino):
    ncaminos = 0
    for i in range(len(matriz_de_caminos)):
        if matriz_de_caminos[i][destino] == 1:
            ncaminos += 1
    return ncaminos
