libros=[[101,"La Llamada de Chuthulu","H. P. Lovecraft","Fantasia"],
        [102,"Berserk Vol1","Kentaro Miura","Fantasia"],
        [103,"Evangelion Vol3","Hideaki Anno","Mechas"],
        [104,"El Regreso del Hijo Pródigo", "Henri J. M. Houwen","Religión"],
        [105,"Gigantomachia Vol1","Kentaro Miura","Novela"]]

def organizar(libro):
    libros_a=[[int(id),nombre[:23],escritor[:15],genero[:8]] for id, nombre, escritor, genero in libro]

    for i in range(len(libros_a)):
        libros_a[i][1]=libros_a[i][1].strip().capitalize()
        libros_a[i][2]=libros_a[i][2].strip().capitalize()
        libros_a[i][3]=libros_a[i][3].strip().capitalize()
    libros_b=sorted(libros_a,key=lambda a: (a[3],a[2],-a[0]))
    return libros_b

def crear(ing):
    ing.append([])
    
    for col in ing[0]:
        ing[len(ing)-1].append(0)
    inter=0
    while inter==0:
        nombre=input("Ingrese el nombre del Libro:")
        escritor=input("Ingrese el Autor del Libro: ")
        genero=input("Ingrese el Genero del libro: ")

        if nombre.isalpha()==True and escritor.isalpha()==True and genero.isalpha()==True:
            inter=1
    ing[-len(ing)][0] = ing[0][0] + 1
    ing[-len(ing)][1] = nombre
    ing[-len(ing)][2] = escritor
    ing[-len(ing)][3] = genero
    
    return ing

def leer(ing):
    print(f"{'ID':>5}{'Nombre':^25}{'Escritor':^20}{'Genero':<5}")
    print("-"*60)

    for id,nombre,escritor,genero in ing:
        print(f"{id:>5}{nombre:^25}{escritor:^20}{genero:<5}")

def actualizar(ing):
    flag=0

    while flag==0:
        print("1- ID")
        print("2- Nombre del Libro")
        print("3- Autor del Libro")
        print("4- Género del Libro")
        ing2=input("Ingrese el dato a actualizar")

        if ing2.isnumeric()==True:
            flag=1
            if ing2==1:
                pos=int(input("Ingresa el ID que deseas cambiar: "))

                band=0
                a=-1

                while band==0 and a<len(ing)-1:
                    a+=1
                    if ing[a][0]==pos:
                        band=1
                if band==1:
                    ing[a][0]==int(input("Ingresa el ID por el que deseas cambiarlo: "))
                    return ing
                else:
                    print("No se encontró el ID")
            else:
                pos= int(input("Ingrese el ID de el Libro a actualizar: "))

                band=0
                a=-1
                while band==0 and a<len(ing)-1:
                    a+=1
                    if ing[a][0]==pos:
                        band=1
                if band==0:
                    print("No se encontró el ID")
                else:
                    print("1- Nombre del Libro")
                    print("2- Nombre del Escritor")
                    print("3- Género del Libro")
                    accion=int(input("Ingrese el valor dependiendo lo que quiera cambiar"))
                    if accion==1:
                        ing[a][1]=input("Ingrese el nombre del Libro: ")
                        return ing
                    elif accion==2:
                        ing[a][2]=input("Ingrese el nombre del Escritor: ")
                        return ing
                    elif accion==3:
                        ing[a][3]=input("Ingrese el Género del Libro: ")
                        return ing
                    else:
                        print("Numero incorrecto")
                        flag=0

def eliminar(ing):
    band=0
    a=-1

    while band==0 and a<len(ing)-1:
        pos=int(input("Ingrese el ID que desea cambiar: "))

        a+=1

        if ing[a][0]==pos and pos.isnumeric()==True:
            ing.pop(a)
            return ing
        else:
            print("No se encontró el ID")
            band=0

def main():
    libros_b=organizar(libros)
    band=0
    flag=-1

    while band==0:
        if flag==0:
            libros_b=organizar(libros)
            flag=-1
        print("1- Crear")
        print("2- Leer")
        print("3- Actualizar")
        print("4- Eliminar")
        print("5- Finalizar")
        accion = int(input("Seleccione una accion: "))
        if accion==1:
            ingresado=crear(libros_b)
            flag=0
        elif accion==2:
            leer(libros_b)
        elif accion==3:
            ingresado=actualizar(libros_b)
            flag=0
        elif accion==4:
            ingresado=eliminar(libros_b)
            flag=0
        elif accion==5:
            band=1
        else:
            print("El numero ingresado no esta dentro de los parametros")
            main()
main()