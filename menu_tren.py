import test as t

###imprimir menu

miubicacion = "Donostia"
mizona = 1

print("***MENU DE RENFE***")
print("1.- Ida\t")
print("2.- Ida y Vuelta\t")
print("3.- Bono Mensual")
opc=input("Su opcion:")

    
if opc=="1":
    ida()
elif opc=="2":
    idayvuelta()
elif opc=="3":
    mensual()
else:
    
    print("Numero incorrecto")


    """elif opc==3:has selecci"""


