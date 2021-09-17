
trigrama ={}


tamanio = 0;

def encontrar(linea):
    for i in range(0,len(linea),3):
        print(linea())
        # tri = linea[i]
        # pos1= tamanio + i
        # pos2= tamanio
        # if ( (i+1 < len(linea)) and ( linea[i+1] == linea[i] ) ):
        #     tri=tri+linea[i+1]
        #     if((i+2 < len(linea)) and ( linea[i+2] == linea[i+1] ) ):
        #         tri=tri+linea[i+2]
        #         pos2 = pos2 + i+2 
        #         i=i+2

    
        # if (len(tri)==3):
        #     if (not trigrama):
        #         trigrama[tri] = []
        #         trigrama[tri].append(pos1) 
        #         trigrama[tri].append(pos2)
        #     else:
        #         trigrama[tri].append(pos1) 
        #         trigrama[tri].append(pos2)

def separacion(trigrama):
    for i in trigrama:
        for j in range(0,len(trigrama[i]),3):
            
            if ( j+3 < len(trigrama[i])):
                print(f"trigramas {i} separados {abs(trigrama[i][j]-trigrama[i][j+3])}")
    
with open("HERALDOSNEGROS_pre.txt") as archivo:
    for linea in archivo:
        encontrar(linea)
        tamanio = tamanio+(len(linea)-1)

# separacion(trigrama)
