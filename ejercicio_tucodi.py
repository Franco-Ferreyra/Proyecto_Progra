import re
"""def main():
    correo=ingresarcorreo()
    print(correo)
def ingresarcorreo():
        print("Tenga en cuenta lo siguiente: nombre@dominio.com")
        correo=input("Ingrese su correo: ")
        patron= r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}+\.[a-zA-Z]{,2}$|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(patron,correo):
            correocorrecto=tuple(creartuplacorreo(correo))
            return correocorrecto
        else:
            print("El correo ingresado es incorrecto.")
            tuplavacia=()
            return tuplavacia
    
def creartuplacorreo(correo):
        correoreemplazado=correo.replace("@",".")
        correoseparado=correoreemplazado.split(".")
        return correoseparado
"""

"""def main():
    texto=ingresartexto()
    texto_o=sorted(texto,key=len)
    print(texto_o)
def ingresartexto():
    texto=input("Ingrese el texto deseado a continuación:\n").replace(",","").replace(".","").split()
    return set(texto)"""

def main():
    dic={"color":"rojo","estado":"No disponible","cantidad":2}
    clave={"color","cantidad"}
    dic_n,cont=eliminador(dic,clave)
    print(dic_n)
    print(cont)
def eliminador(dic,clave):
    cont=0
    for claves in clave:
        del dic[claves]
        cont+=1
    return dic,cont

main()