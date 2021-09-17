# with open("HERALDOSNEGROS_pre.txt") as archivo:
#     for linea in archivo:
#         for i in range(0,len(linea)):
#             if(i+3<len(linea)):
#                 print(linea[i],linea[i+1],linea[i+2])

frase=''
trigrama ={}




def reunir(linea):
    for i in range(0,len(linea)):
        if(i+2<len(linea)):
            tri = linea[i]+linea[i+1]+linea[i+2]
            for j in trigrama:
                if(tri == j):
                    trigrama[j].append(i)
                    trigrama[j].append(i+2)
            # print(linea[i],linea[i+1],linea[i+2])

def encontrar():
    for i in trigrama:
        if (i =='VEL'):
            print(i)
            print(trigrama[i])
        # if (len(trigrama[i])>2):
        #     print(f"tamaño(s) del espacio en {i} son:")
        #     for j in range(0,len(trigrama[i]),2):
        #         if ( j+3 < len(trigrama[i])):
        #             print(f"{abs(trigrama[i][j+1]-trigrama[i][j+3])}")
                    
                
        

with open("HERALDOSNEGROS_pre.txt") as archivo:
    for linea in archivo:
        
        linea = linea.replace('\n',"")
        frase= frase+linea

for i in range(0,len(frase)):
    if(i+2<len(frase)):
        tri = frase[i]+frase[i+1]+frase[i+2]
        trigrama[tri] = []

reunir(frase)
encontrar()
        
# print(trigrama )
# for i in trigrama:
#     print(i)
