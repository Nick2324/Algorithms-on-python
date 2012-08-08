#! /usr/bin/python3.2
#-*- coding: UTF-8


"""
   Este modulo contine las funciones que
   expresan el algoritmo de euclides
"""


def algoritmo_de_euclides_recursivo(a, b):
    if a % b != 0:
        return algoritmo_de_euclides_recursivo(b, a % b)
    else:
        return b


def algoritmo_de_euclides_iterativo(a, b):
    while a % b != 0:
        b, a = a % b, b
    return b
