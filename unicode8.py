print("Texto en ASCII\n\n\n :")
with open("texto.txt") as archivo:
    for linea in archivo:
        print(linea)
        

heraldos = open("HERALDOSNEGROS_pre_2.txt","w")
with open("texto.txt", encoding="utf-8") as archivo:
    cadena = "\n"
    for linea in archivo:
        heraldos.write(linea)
        


heraldos.close()