#!/usr/bin/env python
'''
Listas [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import math


def practica_listas():
    # 1) Crear una lista que contenga los nùmeros del -5 al 5

    # La lista solicitada es una secuencia numérica ordenada, se puede
    # crear utilizando range

    lista1 = []  # Lista vacia

    # Crear una lista de rango -5 a 5 inclusive

    print('1:', lista1)

    # 2) Crear una lista que contengo unicamente los nùmeros
    # impares entre -5 y 5

    lista2 = []  # Lista vacia
    # Crear una lista de rango -5 a 5 inclusive de 
    # solo nùmeros impares

    print('2:', lista2)

    # 3) De la lista1 filtrar los números negativos, es decir,
    # crear una lista a partir de lista1 de solo números negativos

    lista3 = []  # Lista vacia
    # Filtrar numeros negativos


    print('3:', lista3)

    # 4) De la lista1 filtrar los números mayores a 2, es decir,
    # crear una lista a partir de lista1 de solo números mayores a 2

    lista4 = []  # Lista vacia
    # Filtrar numeros mayores a 2
    for n in lista1:
        if n > 3:
            lista4.append(n)

    print('4:', lista4)

    # 5) De la lista1 realizar la suma de todos los números

    suma_total = 0
    # Sumar numeros

    print('5:', suma_total)

    # 6) De la lista1 realizar el modelo, es decir, pasar todos
    # los números a positivo

    lista6 = []  # Lista vacia
    # Aplicar mdulo

    print('6:', lista6)

    # 7) Calcular la suma entre la lista 1 y la lista 6
    # Como son del mismo utilizar len para calcular el largo
    # y recorrer con indices

    lista7 = []  # Lista vacia
    # Sumar listas

    print('7:', lista1)
    print('7:', lista6)
    print('7:', lista7)

    # 8) De la lista1 calcular multiplicar por dos todos los números

    lista8 = []  # Lista vacia
    # Multiplicar por dos

    print('8:', lista8)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    practica_listas()
