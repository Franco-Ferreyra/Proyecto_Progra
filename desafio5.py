import re
matriz=[]
def main():
    crear(matriz)
    leer(matriz)
    
def crear(ing):
    ing.append([])

    for col in ing[0]:
        ing[len(ing)-1].append(0)
    correo=ingresocorreo()
    numero=verificarnum()
    codigo=codigop()
    fecha=validarfecha()

    ing[-len(ing)][0]=ing[0][0]+1
    ing[-len(ing)][1]=correo
    ing[-len(ing)][2]=numero
    ing[-len(ing)][3]=codigo
    ing[-len(ing)][4]=fecha

    return ing

def leer(ing):
    print(f"{'Correo':>5}{'Numero:':^20}{'Codigo Postal':^8}{'Fecha de Nacimiento':<5}")
    print("-"*40)

    for correo,numero,codigo,fecha in ing:
        print(f"{correo:>5}{numero:^20}{codigo:^8}{fecha:<5}")

def ingresocorreo():
    correo=input("Ingrese su correo por favor: ")
    buscar=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+/.[a-zA-Z]{2,}$'
    coincidencia=re.findall(buscar,correo)
    if coincidencia:
        print("El correo fue ingresado con éxito.\n")
        return correo
    else:
        print("El correo ingresado esta mal.")
        print("Recuerde que debe incluir '@' y un '.'")
        print("Ejemplo: pepito@gmail.com")
        ingresocorreo()
    
def verificarnum():
    num=input("Ingrese su número celular: ")
    forma="343 \d{3}-\d{4}|\+54 9 343 \d{3}-\d{4}"
    coincidente=re.fullmatch(forma,num)

    if coincidente:
        print("Su número ha sido ingresado con éxito\n")
        return num
    else:
        print("El número ingresado es incorrecto")
        print("El número debe escribirse como:")
        print("343 XXX-XXXX ó +54 9 343 XXX-XXXX")

        verificarnum()
    

def codigop():
    codigo=input("Ingrese su código postal: ")
    forma=re.compile("\d{4}|[A-Z]{1}\d{4}[A-Z]{3}")
    buscar=forma.findall(codigo)
    if buscar:
        print("Ha ingresado con éxito el código postal\n")
        return codigo
    else:
        print("El código esta mal escrito, recuerde debe ser NNNN o ANNNNAAA")
        codigop()

def validarfecha():
    fecha=input("Ingrese la fecha: ")
    formato=re.compile("\d{4}-\d{2}-\d{2}")
    buscar=formato.findall(fecha)
    if buscar:
        print("Ha ingresado con éxito la fecha")
        return fecha
    else:
        print("La fecha ha sido ingresada erroneamente")
        print("Recuerde que debe ingresarla como YYYY-MM-AA")


main()