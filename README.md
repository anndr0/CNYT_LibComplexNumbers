# Libreria Números Complejos

_En la primera parte encontrarás una librería que contiene las siguientes operaciones con los números complejos:_

1. **Suma**
2. **Producto**
3. **Resta**
4. **División**
5. **Módulo**
6. **Conjugado**
7. **Conversión** entre representaciones polar y cartesiano
8. Retornar la **fase** de un número complejo.

_En la segunda parte encontrarás las siguientes operaciones con los vectores y matrices:_

1. Adición de vectores complejos.
2. Inverso (aditivo) de un vector complejo.
3. Multiplicación de un escalar por un vector complejo.
4. Adición de matrices complejas.
5. Inversa (aditiva) de una matriz compleja.
6. Multiplicación de un escalar por una matriz compleja.
7. Transpuesta de una matriz/vector.
8. Conjugada de una matriz/vector.
9. Adjunta (daga) de una matriz/vector.
10. Producto de dos matrices (de tamaños compatibles).
11. Función para calcular la "acción" de una matriz sobre un vector.
12. Producto interno de dos vectores.
13. Norma de un vector.
14. Distancia entre dos vectores.
15. Revisar si una matriz es unitaria.
16. Revisar si una matriz es Hermitiana.
17. Producto tensor de dos matrices/vectores.

### Pre-requisitos 📋

_Esto necesitaras para correr la librería:_

* Python IDLE (de tu preferencia).
## Ejecutando las pruebas ⚙️

_Lo único que necesitaras es correr el código, ya que las pruebas de la primera parte se encuentran de la siguiente manera:_
```
prettyprinting(sumaCplx(c1, c2))
prettyprinting(restaCplx(c1, c2))
prettyprinting(prodCplx(c1, c2))
prettyprinting(divisionCplx(c1, c2))
print(moduloClpx(c1))
prettyprinting(conjugadoClpx(c1))
prettyprinting(conversionPolarCartesianoClpx(c1))
polprettyprinting(conversionCartesianoPolarClpx(c1))
print(faseClpx(c1))
```
_Y se aplican a estos números complejos:_

```
c1 = (2, -1)
c2 = (-1, 3)
```

_Obteniendo como resultado,_
```
1+2i
3-4i
1+7i
-0.5-0.5i
2.24
2+1i
1-1.68i
2.24 e^(i -0.46)
-0.46
```
_Segundas pruebas:_
```
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
```
_Y se aplican a:_

```
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
```

_Obteniendo como resultado,_
```
[22-1.7i, 7-4i, 10.2-8.1i, 0-7i]
[-6 + 4.0i, -7-3i, -4.2 + 8.1i, 0 + 3.0i]
[12 + 21i, 0 + 0i, 13 + 13i, 12 + 8i]
[[(2, 2), (2, 2), (2, 2)], [(2, 2), (2, 2), (2, 2)], [(2, 2), (2, 2), (2, 2)]]
[[(-1, -1), (-1, -1), (-1, -1)], [(-1, -1), (-1, -1), (-1, -1)], [(-1, -1), (-1, -1), (-1, -1)]]
[[(0, -4), (0, -4), (0, -4)], [(0, -4), (0, -4), (0, -4)], [(0, -4), (0, -4), (0, -4)]]
[[(3, 2), (9, 5), (4, 2)], [(4, 1), (3, 4), (7, 2)], [(2, 5), (1, 6), (9, 6)]]
[[(3, 2), (4, -1), (2, 5)], [(9, -5), (3, 4), (1, -6)], [(4, 2), (7, -2), (9, 6)]]
[[(3, -2), (4, 1), (2, -5)], [(9, 5), (3, -4), (1, 6)], [(4, -2), (7, 2), (9, -6)]]
[[(3, -2), (9, 5), (4, -2)], [(4, 1), (3, -4), (7, 2)], [(2, -5), (1, 6), (9, -6)]]
[[(26, -52), (60, 24), (26, 0)], [(9, 7), (1, 29), (14, 0)], [(48, -26), (14, 20), (16, -28)]]
[(18, -4), (16, 7)]
11
5.0
3.3166247903554
```
## Autor ✒️

* **Ana María Durán Burgos** - *Librería Operaciones con Números Complejos* - [anndr0](https://github.com/anndr0)

