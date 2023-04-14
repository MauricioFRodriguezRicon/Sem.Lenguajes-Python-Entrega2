nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#A)
def generarEstructura():
    lista = nombres.replace("'","").replace("\n","").replace(" ","").split(",")
    alumnos = list(zip(lista,notas_1,notas_2))
    print('Las notas de los estudiantes son ',alumnos)
    return alumnos
#B)

promedio = lambda a,b: (a+b)/2

def agregar(promedios,alumno):
    promedios.append([alumno[0],promedio(alumno[1],alumno[2])])

def calcularPromedios(alumnos):
    promedios = []
    for alu in alumnos:
        agregar(promedios,alu)
    print('Los promedios de cada estudiante son',promedios)
    return promedios
#C)
def promedioTotal(promedios):
    total = 0
    for alu in promedios:
        total+= alu[1]
    print('El promedio de el grupo es ',round(total/len(promedios),2))


#D)
def maximo(promedios):
    notas=[]
    for prom in promedios:
        notas.append(prom[1])
    i = notas.index(max(notas))
    print('El alumno con el promedio mas alto es ',promedios[i][0],' con un promedio de ', round(promedios[i][1],2))

#E)
def minimo(alumnos):
    notas_min = []
    for alu in alumnos:
        notas_min.append(min(alu[1],alu[2]))
    i = notas_min.index(min(notas_min))
    print('El alumno con la nota mas baja es ',alumnos[i][0],' con una nota de ',notas_min[i])


#PP)
alumnos = generarEstructura()
promedios = calcularPromedios(alumnos)
maximo(promedios)
minimo(alumnos)