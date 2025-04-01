import numpy as np

def esUno(matrizA,n1,n2):
    return matrizA[n1][n2] == 1

def ResolverXY(matrizA,tam,x1,y1):
    # Volver uno el pivote
    if matrizA[x1][y1] == 0:
        print(f"Error: pivote cero en posición ({x1+1},{y1+1}). Se requiere pivoteo.")
        return

    if not esUno(matrizA,x1,y1):
        pivote = matrizA[x1][y1]
        for y in range(tam+1):
            matrizA[x1][y] = matrizA[x1][y] / pivote

    # Eliminar toda la columna
    for x in range(tam):
        if x != x1:
            cof = matrizA[x][y1]
            for y in range(tam+1):
                matrizA[x][y] -= cof * matrizA[x1][y]

def Resolver(matrizA,tam):
    for z in range(tam):
        ResolverXY(matrizA,tam,z,z)

# Entrada
tam = int(input("Ingresa la cantidad de ecuaciones: "))
matrizA = np.zeros((tam, tam+1))

for x in range(tam):
    for y in range(tam+1):
        matrizA[x][y] = float(input(f"Ingresa el valor de a{x+1}{y+1}: "))

Resolver(matrizA,tam)

# Resultado
print("\nMatriz escalonada reducida (Gauss-Jordan):")
print(matrizA)

print("\nSoluciones:")
for i in range(tam):
    print(f"x{i+1} = {round(matrizA[i][-1],2)}")
