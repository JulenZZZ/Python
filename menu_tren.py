import test as t

###imprimir menu

miubicacion = "Donostia"
mizona = 1
print("***MENU DE RENFE***")
print("1.- Ida\t")
print("2.- Ida y Vuelta\t")
print("3.- Bono Mensual")
opc=input("Su opcion:")
int(opc)
    
if opc==1:
    ida()
elif opc==2:
    idayvuelta()
elif opc==3:
    mensual()
else:
    
    print("Numero incorrecto")


    """elif opc==3:has selecci"""


def ida():
    destino=input("Seleccione su destino:")
    destino.title()

   # for destino,z in zonas.items():
      # if destino == p:
       #    """ return """
    for z,v in t.zonas.items():
        for d in v:
            if d==destino:
                mizona==z
                break

    t.precios[opc][abs(z-mizona)]



def idayvuelta():
    destino=input("Seleccione su destino:")
    destino.title()
    
    for z,v in t.zonas.items():
        for d in v:
            if d==destino:
                mizona==z
                break

    t.precios[opc][abs(z-mizona)]

def mensual():
    print("este es el mensual.")








