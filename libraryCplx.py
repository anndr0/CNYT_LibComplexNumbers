import math
''' ------------ Primera Entrega ------------ '''
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
    else:
        numImg = numImg
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
print()
print('------------  COMIENZO PRUEBAS PRIMERA ENTREGA ------------')
prettyprinting(sumaCplx(c1, c2))
prettyprinting(restaCplx(c1, c2))
prettyprinting(prodCplx(c1, c2))
prettyprinting(divisionCplx(c1, c2))
print(moduloClpx(c1))
prettyprinting(conjugadoClpx(c1))
prettyprinting(conversionPolarCartesianoClpx(c1))
polprettyprinting(conversionCartesianoPolarClpx(c1))
print(faseClpx(c1))
print()
print('------------  FINAL PRUEBAS PRIMERA ENTREGA ------------')
print()

''' ------------ Segunda Entrega ------------'''

def prettyPrinting(v1, v2):
    final = []
    c1String = list(map(str, v1))
    c2String = list(map(str, v2))

    for i in range(len(c1String)):
        if v2[i] < 0:
            union = c1String[i] + c2String[i] + 'i'
        else:
            union = c1String[i] + ' + ' + c2String[i] + 'i'
        final.append(union)
    print('[%s]' % ', '.join(map(str, final)))


def adicionVectores(v1, v2):
    # 1. Adición de vectores complejos.
    sumaReal, sumaImg, suma1, suma2 = [], [], 0, 0

    for i in range(len(v1)):
        suma1 = v1[i][0] + v2[i][0]
        sumaReal.append(round(suma1, 2))

        suma2 = v1[i][1] + v2[i][1]
        sumaImg.append(round(suma2, 2))
    prettyPrinting(sumaReal, sumaImg)


def inversoAditivo(v1):
    # 2. Inverso (aditivo) de un vector complejo.
    numReal, numImg, final = [], [], []
    for i in range(len(v1)):
        if v1[i][0] < 0:
            absValR = math.fabs(v1[i][0])
            numReal.append(absValR)
        else:
            negValR = v1[i][0]
            numReal.append(negValR * (-1))

        if v1[i][1] < 0:
            absValI = math.fabs(v1[i][1])
            numImg.append(round(absValI, 2))
        else:
            negValI = v1[i][1]
            numImg.append(round(negValI * (-1), 2))
    prettyPrinting(numReal, numImg)

def multiEscalarVector(c, v):
    # 3. Multiplicación de un escalar por un vector complejo.
    multi, vnumReal, vnumImg = [], [], []
    for i in range(len(v)):
        byScalar = prodCplx(c, v[i])
        multi.append(byScalar)

    # for para se parar en vectores y llevarlos a la función imprimir
    for i in range(len(multi)):
        numReal = multi[i][0]
        vnumReal.append(numReal)
        numImg = multi[i][1]
        vnumImg.append(numImg)
    prettyPrinting(vnumReal, vnumImg)

def adicionMatrices(mat1, mat2):
    # 4. Adición de matrices complejas.
    newMat = [[0 for j in range(len(mat1[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            newMat[i][j] = sumaCplx(mat1[i][j], mat2[i][j])
    print(newMat)

def inversaMatriz(mat1):
    # 5. Inversa (aditiva) de una matriz compleja.
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j] = ((-1) * mat1[i][j][0], (-1) * mat1[i][j][1])
    print(mat1)

def escalarMatriz(c, A):
    # 6. Multiplicación de un escalar por una matriz compleja.
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = prodCplx(c, A[i][j])
    print(A)

def tranpuestaMatriz(mat):
    # 7. Transpuesta de una matriz/vector
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j < i:
                nueva = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = nueva
    print(mat)

def conjugadaMatriz(mat):
    # 8. Conjugada de una matriz/vector
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] = mat[i][j][0], (-1) * mat[i][j][1]
    print(mat)

def adjuntaMatriz(mat):
    # 9. Adjunta (daga) de una matriz/vector
    matriz = conjugadaMatriz(mat)
    matriz = tranpuestaMatriz(mat)
    print(matriz)

def multiplicacionMatrices(mat1, mat2):
    # 10. Producto de dos matrices (de tamaños compatibles)
    multiMat = [[0 for j in range(len(mat1))] for i in range(len(mat2[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            res = (0, 0)
            for k in range(len(mat2)):
                c1 = mat2[k][j]
                c2 = mat1[i][k]
                res = sumaCplx(res, prodCplx(c1, c2))
            multiMat[i][j] = res
    print(multiMat)

def accionMatrizVector(v, mat):
    # 11. Función para calcular la "acción" de una matriz sobre un vector.
    mat0 = [0 for i in range(len(v))]
    for i in range(len(v)):
        res = (0, 0)
        for j in range(len(v)):
            c1 = mat[i][j]
            c2 = v[j]
            res = sumaCplx(res, prodCplx(c1, c2))
        mat0[i] = res
    print(mat0)

def productoInternoVectores(v1, v2):
    # 12. Producto interno de dos vectores
    productoInterno = 0
    for i in range(len(v1)):
        productoInterno += v1[i] * v2[i]
    print(productoInterno)

def normaVector(v):
    # 13. Norma de un vector
    suma = 0
    for i in range(len(v)):
        suma += v[i] ** 2
    raiz = math.sqrt(suma)
    print(raiz)

def distanciaVectores(v1, v2):
    # 14. Distancia entre dos vectores
    resta, cuadrado, suma = [], [], 0
    for i in range(len(v1)):
        resta1 = v1[i] - v2[i]
        resta.append(resta1)

    for i in range(len(resta)):
        cuadrados = resta[i] ** 2
        cuadrado.append(cuadrados)

    for i in range(len(cuadrado)):
        suma += cuadrado[i]
    res = math.sqrt(suma)
    print(res)

def revMatrizUnitaria(mat):
    # 15. Revisar si una matriz es unitaria
    matriz = multiplicacionMatrices(mat, adjuntaMatriz(mat))
    print(matriz)


# Para operaciones entre vectores
v1 = [(6, -4), (7, 3), (4.2, -8.1), (0, -3)]
v2 = [(16, 2.3), (0, -7), (6, 0), (0, -4)]

# Función multiEscalarVector
c = (3, 2)
v = [(6, 3), (0, 0), (5, 1), (4, 0)]

# Para operaciones entre matrices
mat1 = [[(1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1)]]
mat2 = [[(1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1)]]
mat3 = [[(3, 2), (4, 1), (2, 5)], [(9, 5), (3, 4), (1, 6)], [(4, 2), (7, 2), (9, 6)]]

# Para probar la conjugada
mat4 = [[(3, -2), (4, 1), (2, -5)], [(9, 5), (3, -4), (1, 6)], [(4, -2), (7, 2), (9, -6)]]

# Para multiplicación entre matrices
mat5 = [[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -2), (0, 0), (4, 0)]]
mat6 = [[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]

# Para escalarMatriz
c1 = (2, 2)

# Para accion Matriz Vector
vec = [(2, 1), (4, -1)]
mat7 = [[(2, 1), (4, -1)], [(5, 2), (2, 0)]]

# Para producto interno
vq = [8, 3, 7]
vr = [0, -1, 2]

print()
print('------------  INICIO PRUEBAS SEGUNDA ENTREGA ------------')
# Pruebas
'''1. Adición de vectores complejos.'''
adicionVectores(v1, v2)

'''2. Inverso (aditivo) de un vector complejo.'''
inversoAditivo(v1)

'''3. Multiplicación de un escalar por un vector complejo.'''
multiEscalarVector(c, v)

'''4. Adición de matrices complejas.'''
adicionMatrices(mat1, mat2)

'''5. Inversa (aditiva) de una matriz compleja.'''
inversaMatriz(mat1)

'''6. Multiplicación de un escalar por una matriz compleja.'''
escalarMatriz(c1, mat1)

'''7. Transpuesta de una matriz/vector'''
tranpuestaMatriz(mat3)

'''8. Conjugada de una matriz/vector'''
conjugadaMatriz(mat4)

'''9. Adjunta (daga) de una matriz/vector'''
adjuntaMatriz(mat4)

'''10. Producto de dos matrices (de tamaños compatibles)'''
multiplicacionMatrices(mat5, mat6)

'''11. Función para calcular la "acción" de una matriz sobre un vector.'''
accionMatrizVector(vec, mat7)

'''12. Producto interno de dos vectores'''
productoInternoVectores(vq, vr)

''' 13. Norma de un vector'''
v11 = [3, 4]
normaVector(v11)

''' 14. Distancia entre dos vectores'''
vd1 = [3, 1, 2]
vd2 = [2, 2, -1]
distanciaVectores(vd1, vd2)
print()
print('------------  FINAL PRUEBAS SEGUNDA ENTREGA ------------')