contador = 0

def colocar(linea):
    global contador
    aux = linea
    separa = 0
    for i in range(0,len(linea)): 
        if(linea[i] == " " or linea[i] == "\n"):
            # separa = separa+1
            continue
        contador = contador+1
        if(contador%20 == 0):
            # print(f"{i} {linea[i]}   {contador} {separa} {aux[i]}  ")
            x = i+separa
            # print(f"{x}")
            # print(aux)
            if(x < len(aux)-1):
                # print(aux[x])
                aux = aux[:x+1]+'AQUI'+aux[x+1:]
                separa = separa +4
    aux2 = aux.split()
    for i in range(0,len(aux2)):
        if(aux2[i].find('AQUI')>0):
            # print(len(aux2[i]))
            # aux2[i] = aux2[i]+'x'
            while (len(aux2[i])%4 != 0):
                aux2[i] = aux2[i]+'x'
    # aux2 = ' '.join(aux2)
    # print(aux2)
    return (' '.join(aux2))
    
aqui = open("AQUI_pre.txt","w")
with open("texto.txt", encoding="utf-8") as archivo:
    cadena = "\n"
    for linea in archivo:
        aqui.write(colocar(linea)+"\n")
        # print (linea[:4]+"HOLA"+linea[4:])
        # print(linea[4])
aqui.close()
# print(contador)