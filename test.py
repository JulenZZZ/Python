zonas={1: ["Urnieta","Hernani","Martutene","Loiola","Donostia","Gros","Ategorrieta"],
        2:["Andoain","Lezo","Irun"],
        3:["Tolosa","Tolosa Erdia"," Anoeta","Billabona"],
        4:["Ikaztegieta","Legorreta","Itsasondo","Ordizia"],
        5:["Ormaiztegi","Zumarraga","Legazpi"]}

precios= {
        1: [1.70,1.90,2.60,3.35,3.80,5.0],
        2: [2.60,2.75,4.10,5.50,6.49],
        3: [34.32,45,56,78,88,99]
} 
def ida():
    print("Has seleccionado")
    print(t.zonas)
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

    print(t.precios[opc][abs(int(z)-mizona)])

def idayvuelta():
    print(t.zonas)
    
    destino=input("Seleccione su destino:")
    destino.title()
    
    for z,v in t.zonas.items():
        for d in v:
            if d==destino:
                mizona==z
                break

    print(t.precios[opc][abs(int(z)-mizona)])

def mensual():
    print("este es el mensual.")

def print_zonas(zona):
    return zona[zona]

def print_preciosIda():
        return precios[1]
def print_preciosIdaVuelta():
        return precios[2]
def print_preciosMensual():
        return precios[3]


"""print(zonas["zona1"]["ida"])"""

#imprime todos los destinos de la zona uno
#def imprime_zonas():
 #   for i in zonas.values():
  #      print (i)
   #     print(i["zona1"])
#imprime_zonas()

