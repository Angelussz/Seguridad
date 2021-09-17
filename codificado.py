def remplazo(linea):
    nlinea = linea.lower()
    nlinea = nlinea.replace('j','i')
    nlinea = nlinea.replace('h','i')
    nlinea = nlinea.replace('ñ','n')
    nlinea = nlinea.replace('k','l')
    nlinea = nlinea.replace('u','v')
    nlinea = nlinea.replace('w','v')
    nlinea = nlinea.replace('y','z')
    
            
    return nlinea     
    
def elimtilde(linea):
    nlinea = linea
    nlinea = nlinea.replace('á','a')
    nlinea = nlinea.replace('é','e')
    nlinea = nlinea.replace('í','i')
    nlinea = nlinea.replace('ó','o')
    nlinea = nlinea.replace('ú','u')
    return nlinea
    
def mayusculas(linea):
    nlinea = linea
    nlinea = nlinea.upper()
    return nlinea

def espacios(linea):
    nlinea = linea
    nlinea = nlinea.replace(' ','')
    return nlinea

heraldos = open("HERALDOSNEGROS_pre.txt","w")
with open("texto.txt", encoding="utf-8") as archivo:
    cadena = "\n"
    for linea in archivo:
        if (linea != cadena):
            linea = remplazo(linea)
            linea = elimtilde(linea)
            linea = mayusculas(linea)
            linea = espacios(linea)
            heraldos.write(linea)
        


heraldos.close()
        
