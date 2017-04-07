zonas={1: ["Urnieta","Hernani","Martutene","Loiola","Donostia","Gros","Ategorrieta"],
        2:["Andoain","Lezo","Irun"],
        3:["Tolosa","Tolosa Erdia"," Anoeta","Billabona"],
        4:["Ikaztegieta","Legorreta","Itsasondo","Ordizia"],
        5:["Ormaiztegi","Zumarraga","Legazpi"]}

precios= {
        1: [1.70,1.90,2.60,3.35,3.80],
        2: [2.60,2.75,4.10,5.50,6.40],
        3: [34.45,43.95,58.65,73.30,85.80]
} 
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

    print(precios[opc][abs(int(z)-mizona)])

def idayvuelta():

    
    destino=input("Seleccione su destino:")
    destino.title()
    
    for z,v in t.zonas.items():
        for d in v:
            if d==destino:
                mizona==z
                break

    return (precios[opc][abs(int(z)-mizona)])

def mensual():
    return("Este es el mensual.")

def print_zonas():
    #estaciones=[]
    c_estaciones=""
    for z,p in zonas.items():
        for s in p:
            c_estaciones+='<a href="#" >'+s+'</a> <br>'

    return c_estaciones


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

