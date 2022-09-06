import math

def sumaCplx(c1, c2):
    # Suma complejos representados como una tupla
    numReal = c1[0] + c2[0]
    numImg = c1[1] + c2[1]
    res = numReal, numImg
    return res


def prodCplx(c1, c2):
    # Multiplica complejos representados como una tupla
    a1a2 = c1[0] * c2[0]
    b1b2 = c1[1] * c2[1]
    a1b2 = c1[0] * c2[1]
    a2b1 = c2[0] * c1[1]
    multiplication = (a1a2 - b1b2, a1b2 + a2b1)
    return multiplication

def restaCplx(c1, c2):
    # Resta complejos representados como una tupla
    numReal = c1[0] - c2[0]
    numImg = c1[1] - c2[1]
    res = numReal, numImg
    return res


def divisionCplx(c1, c2):
    # Divide complejos representados como una tupla
    a1a2 = c1[0] * c2[0]
    b1b2 = c1[1] * c2[1]
    a1b2 = c1[0] * c2[1]
    a2b1 = c2[0] * c1[1]
    a2 = (c2[0]) ** 2
    b2 = (c2[1]) ** 2

    Parte1 = a2 + b2
    Parte2 = a1a2 + b1b2
    Parte3 = a2b1 - a1b2

    return (round(Parte2 / Parte1, 2), round(Parte3 / Parte1, 2))


def moduloClpx(c1):
    # Saca el modulo de un complejo representado como una tupla
    module = math.sqrt(((c1[0]) ** 2 + (c1[1]) ** 2))
    return round(module, 2)


def conjugadoClpx(c1):
    # Conjugado de un número representado como una tupla
    numReal = c1[0]
    numImg = c1[1]

    if numImg < 0:
        numImg = abs(numImg)
    return (numReal, numImg)


# Conversión entre representaciones polar y cartesiano
def conversionPolarCartesianoClpx(c1):
    a = c1[0] * math.cos(c1[1])
    b = c1[0] * math.sin(c1[1])
    return (round(a), round(b, 2))


def conversionCartesianoPolarClpx(c1):
    a = c1[0]
    b = c1[1]
    rho = math.sqrt(a ** 2 + b ** 2)
    theta = math.atan(b / a)
    return (round(rho, 2), round(theta, 2))


def faseClpx(c1):
    # Retornar la fase de un número complejo.
    a = c1[0]
    b = c1[1]
    theta = math.atan(b / a)
    return round(theta, 2)


def prettyprinting(c):
    # Para cartesianos
    if c[1] < 0:
        print(str(c[0]) + str(c[1]) + "i")
    elif c[1] == 0:
        print(str(c[0]))
    else:
        print(str(c[0]) + "+" + str(c[1]) + "i")


def polprettyprinting(c):
    # Para polares
    print(str(c[0]) + " e^(i " + str(c[1]) + ")")


c1 = (2, -1)
c2 = (-1, 3)

prettyprinting(sumaCplx(c1, c2))
prettyprinting(restaCplx(c1, c2))
prettyprinting(prodCplx(c1, c2))
prettyprinting(divisionCplx(c1, c2))
print(moduloClpx(c1))
prettyprinting(conjugadoClpx(c1))
prettyprinting(conversionPolarCartesianoClpx(c1))
polprettyprinting(conversionCartesianoPolarClpx(c1))
print(faseClpx(c1))
#hola
print()