import archivoArff as fichero
import procesarImagen

def escrbirFichero(nombre):
    fichero.abrirFichero(nombre + ".arff")
    fichero.relation(nombre)
    fichero.attribute("hu1", "numeric")
    fichero.attribute("hu2", "numeric")
    fichero.attribute("hu3", "numeric")
    fichero.attribute("hu4", "numeric")
    fichero.attribute("hu5", "numeric")
    fichero.attribute("hu6", "numeric")
    fichero.attribute("hu7", "numeric")
    fichero.attribute("tipo", "{mano, noMano}")
    fichero.empezarDatos()

def aniadirDatos(carpeta, tipo):
    for foto in carpeta:
        imagen, hu = procesarImagen.procesar(foto)
        #procesarImagen.imprimirImagen(imagen, foto)
        array = []
        for h in hu:
            array.append(h[0])
        array.append(tipo)
        fichero.escribirDatosArray(array)


manos = procesarImagen.ls('manos')
noManos = procesarImagen.ls('noManos')

escrbirFichero("manos")

aniadirDatos(manos, "mano")
aniadirDatos(noManos, "noMano")


fichero.cerrarFichero()