import procesarImagen as pi

def reglas(hu):
    #print(hu)
    if hu[4] <= 0.000019:
        return False
    else:
        if hu[2] <= 0.026982:
            return True
        else:
            return False
        

def imprimirConsola(imagen, resultado):
    print(imagen + " " + str(resultado))

def imprimirGrafico(imagen, resultado):
    pi.imprimirImagen(imagen, resultado)

def clasificarCarpeta(carpeta):
    test = pi.ls(carpeta)
    for i in range(len(test)):
        im, hu = pi.procesar(test[i])
        array = []
        array.append(0)
        for h in hu:
            array.append(h[0])
        imprimirConsola(test[i], reglas(array))
        #print(array)
        #imprimirGrafico(im, reglas(array))

clasificarCarpeta("noManos")