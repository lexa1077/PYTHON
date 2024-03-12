print("ESTRUCTURAS DE DATOS")
#diccionario = {00101:"CAJA PAPAS GRANDE POLIPAPEL  EPP",
#00109:	"CONTENEDOR 24 ONZ EPS X20 UN DN",
#00165:	"DOMO CONT DOBLE USO 12 ONZ CRISTAL DN,"
#00166:	"DOMO CONT DOBLE USO 16 ONZ NEGRO DN",
#00167:	"DOMO CONT DOBLE USO 24 ONZ CRISTAL DN"}


""" 
print("Listas")

numeros = [1,2,3,4,5,6]
nombre = ["Alex","Andrea","Mia","Gerardo","Genesis","Itzel"]

matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]


matrix2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

suma_matrices=[]

for i in range(len(matrix1)):
    suma = []
    for j in range(len(matrix1)):
        #print(matrix1[i]+[matrix2[j]])
        resultado = matrix1[i]+[matrix2[j]]
        suma.append(resultado)
    suma_matrices.append(suma)



#print(suma_matrices)
for i in suma_matrices:
    print(i)
 """




# Escriba un programa que permita multiplicar únicamente matrices de 2 filas por 2 columnas.
# Veamos un ejemplo concreto:
# A = [[6, 4], [8, 9]]
# B = [[3, 2], [1, 7]]

""" A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

suma_matrices =[]


for i in range(len(A)):
    sumas =[]
    for j in range(len(A)):
        resultado = A[i][j]+B[i][j]
        sumas.append(resultado)
    suma_matrices.append(sumas)


#rrecorremos la matriz
for i in suma_matrices:
    print(i)

 """







# nombres_por_categoria = [
#     ["Juan","Alex","María", "Carlos"],#0
#     ["Laura", "Pedro","Andrea"],#1
#     ["Ana", "Diego", "Elena"]#2
# ]


# # Definimos las matrices
# #matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# matrix1= [[6, 4], [8, 9]]
# matrix2 = [[3, 2], [1, 7]]

# # Inicializamos una nueva matriz para almacenar la suma
# suma_matrices = []

# # Iteramos sobre las filas de las matrices
# for i in range(len(matrix1)):
#     fila_suma = []  # Inicializamos una lista para almacenar la fila de la suma
#     for j in range(len(matrix1[0])):
#         # Sumamos los elementos correspondientes de ambas matrices y los añadimos a la fila de suma
#         suma_elemento = matrix1[i][j] + matrix2[i][j]
#         fila_suma.append(suma_elemento)
#     # Agregamos la fila de suma a la matriz de suma
#     suma_matrices.append(fila_suma)

# # Imprimimos la matriz de suma
# for fila in suma_matrices:
#     print(fila)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]



matriz_suma = []


for i in range(len(matrix1)):#Asignamos el primer bucle
    sumas = []#Creamos matriz donde se guardan las sumas
    for j in range(len(matrix1)):#creamos el segundo ciclo
        print(str(matrix1[i][j])+" + " + str(matrix2[i][j]))
        resultados = matrix1[i][j]+ matrix2[i][j]#hacemos las operaciones

        sumas.append(resultados)#Agregamos el resultado a la operacion y saltamos
    matriz_suma.append(sumas)#agregamos las lista a las sumas


""" for i in matriz_suma:
    print(i) """