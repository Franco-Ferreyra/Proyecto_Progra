import random
materias=["Nombres","m1","m2","m3","m4"]
alumnos=["Pepe","Martín","Agustín","María","Pedro"]
matriz=[]
def main():
    crearmatriz(materias,alumnos)
    generarnotas(materias,alumnos,matriz)
    muestradematriz(matriz)
    promedio(materias,alumnos,matriz)

def crearmatriz(a,b):
    for fil in range(len(alumnos)+1):
        matriz.append([])
        for col in range(len(materias)):
            matriz[fil].append(0)

def generarnotas(a,b,c):
    temp=-1
    for i in range(len(c)):
        for x in range(len(c[0])):
            if i==0:
                c[i][x]=a[x]
            elif x==0:
                c[i][x]=b[temp]
        temp+=1
    for j in range(1,len(c)):
        for i in range(1, len(c[0])-1):
            c[j][i]=random.randint(0,10)

def muestradematriz(a):
    for i in range(len(a)):
        for x in range(len(a[0])):
            print(matriz[i][x],end="  ")
        print()

def promedio(a,b,c):
    suma=0
    for i in range(1,len(a)):
        for j in range(1,len(b[0])):
            suma+=c[i][j]
    total_elementos=(len(a)-1)*(len(b)-1)
    promedio=suma/total_elementos
    print("El promedio es: ", promedio)

main()