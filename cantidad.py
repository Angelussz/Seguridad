import operator

tabla_frecuencia = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
    }

def cantidad(linea):
    for valor in linea:
        if(valor.isalpha()):
            tabla_frecuencia[valor] = tabla_frecuencia[valor]+1 
        else:
            continue



with open("HERALDOSNEGROS_pre.txt") as archivo:
    for linea in archivo:
        cantidad(linea)
        
    


frecuencias = sorted(tabla_frecuencia.items(), key=operator.itemgetter(1), reverse=True)

print('Letra   |      Cantidad')
print('_______________________')
for name in enumerate(frecuencias):
    print(name[1][0], '      |       ', tabla_frecuencia[name[1][0]])


