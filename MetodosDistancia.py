import math

def distanciaEuclidiana(x, y):
    resta= [(a - b) ** 2 for a, b in zip(x, y)]
    return math.sqrt(sum(resta))

def distanciaManhattan(x, y):
    resta = [abs(a - b) for a, b in zip(x, y)]
    return sum(resta)

def distanciaMinkowski(x, y, p):
    resta = [abs(a - b) ** p for a, b in zip(x, y)]
    return sum(resta) ** (1/p)