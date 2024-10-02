import math
import random
lista=[]
"""def main():  
    try:
        num=int(input("Ingrese un número cuadrado: "))
        print(math.sqrt(num))
    except(ValueError):
        print("Ingrese un alor adecuado")"""

"""def main():
    ing=0
    ruptura=0
    while ing!=-1:
        ing=int(input("Ingresar el dígito solicitado"))
        if ing!=-1:
            lista.append(ing)
        else:
            break
    print(lista)
    while True:
        if ruptura==3:
            print("Ha fallado demasiadas veces, cerrando programa.")
            break
        try:
            busc=int(input("Ingrese el valor que desea buscar: "))
            lista.index(busc)
        except(ValueError):
            print("Ingrese un valor adecuado")
            ruptura+=1
            continue
        else:
            print("El valor esta en la lista")
            break"""

"""def main():
    num=random.randint(1,500)
    print(num)
    intentos=0
    while True:
        try:
            busc=int(input("Ingrese el número que supone es"))
        except (ValueError):
            print("Ingrese un valor adecuado")
            intentos+=1
            continue
        if busc<num:
            print("El número ingresado es mas grande que el que buscas")
            intentos+=1
            continue
        elif busc>num:
            print("El número que buscas es mas pequeño que el indicado")
            intentos+=1
            continue
        else:
            print(f"¡Felicidades, encontraste el número! Te tomó {intentos+1} intentos")
            break"""

        


main()
    
